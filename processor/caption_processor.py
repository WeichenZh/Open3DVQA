import os
import cv2
import sys
import json
import numpy as np
sys.path.append('../')
from AirsimToolBox.airsim_utils.coords_conversion import *
from utils.bbox_utils import calc_iou, calc_vis_iou


def select_obj_by_range(ego_loc, objs, range_threshold=50):
    selected_obj = {}
    for obj_id in objs:
        obj_loc = np.array(objs[obj_id]['actor_loc']).reshape(1, -1)
        obj_loc = ue_world2airsim_world(obj_loc)
        ego_range = np.linalg.norm((obj_loc - ego_loc))
        if ego_range < range_threshold:
            objs[obj_id]['ego_range'] = ego_range
            selected_obj[obj_id] = objs[obj_id]

    return selected_obj


def select_obj_by_visible_bbox(objs, img_width, img_height, outsight_threshold=0.8, nms_threshold=0.5):
    ids = []
    dists = []
    bboxes = []
    # for obj_id in objs:
    #     ids.append(obj_id)
    #     dists.append(objs[obj_id]['ego_range'])
    #     bboxes.append(objs[obj_id]['bbox_2d'])

    # filter out-of-sight bbox
    for obj_id in objs:
        oid = objs[obj_id]['actor_id']
        dist = objs[obj_id]['ego_range']
        bbox = objs[obj_id]['bbox_2d']

        bbox2 = np.zeros(4)
        bbox2[0] = max(0, min(img_width, bbox[0]))
        bbox2[1] = max(0, min(img_height, bbox[1]))
        bbox2[2] = max(0, min(img_width, bbox[2]))
        bbox2[3] = max(0, min(img_height, bbox[3]))

        iou = calc_iou(bbox2, bbox)
        if iou > outsight_threshold:
            ids.append(oid)
            dists.append(dist)
            bboxes.append(bbox)

    # nms: select the closest object and filter overlapped bbox
    indices = np.argsort(dists)[:]
    selected_bbox = []
    selected_ids = []
    while len(indices) > 0:
        # 选择当前得分最高的框
        current_index = indices[0]
        current_box = bboxes[current_index]
        current_id = ids[current_index]

        # 保留该框
        selected_bbox.append(current_box)
        selected_ids.append(current_id)

        # 计算与其他框的IoU
        remaining_ids = []
        remaining_boxes = []
        remaining_indices = []

        for i in range(1, len(indices)):
            iou = calc_vis_iou(current_box, bboxes[indices[i]])
            if iou < nms_threshold:
                remaining_ids.append(ids[indices[i]])
                remaining_boxes.append(bboxes[indices[i]])
                remaining_indices.append(indices[i])

        # 更新框列表，只保留IoU低于阈值的框
        # ids = remaining_ids
        # bboxes = remaining_boxes
        indices = remaining_indices

    return [objs[obj_id] for obj_id in selected_ids]


def project_bbox2view(objs, obs_point_path):
    states = os.listdir(os.path.join(obs_point_path, "state"))
    rgb_imgs = os.listdir(os.path.join(obs_point_path, "rgb"))
    # os.makedirs(os.path.join(obs_point_path, "boundingbox_images"), exist_ok=True)
    # bounding_boxes_imgs = os.listdir(os.path.join(obs_point_path, "boundingbox_images"))

    for i in range(len(states)):
        assert states[i].split(".")[0] == rgb_imgs[i].split(".")[0], "state and rgb names do not match"
        state_path = os.path.join(obs_point_path, "state", states[i])
        rgb_path = os.path.join(obs_point_path, "rgb", rgb_imgs[i])

        img = cv2.imread(rgb_path)
        height, width = img.shape[:2]

        with open(state_path, "r") as f:
            state = json.load(f)
        pos = np.array(state["translation"])
        ori = np.array(state["rotation"][1:] + state["rotation"][0:1])   # [w, x, y, z] -> [x, y, z, w]

        for obj_id in objs:
            obj_loc = np.array(objs[obj_id]["actor_loc"]).reshape(1, -1)
            rel_obj_loc = ue_world2airsim_world(obj_loc)
            rel_obj_loc = airsim_world2airsim_ego(rel_obj_loc, pos, ori)
            rel_obj_loc = airsim_ego2camera(rel_obj_loc)
            objs[obj_id]["cam_obj_loc"] = rel_obj_loc.tolist()

            bbox = np.array(objs[obj_id]["actor_bbox_3d"])

            bbox_coords = ue_world2airsim_world(bbox)
            bbox_coords = airsim_world2airsim_ego(bbox_coords, pos, ori)
            bbox_coords = airsim_ego2camera(bbox_coords)
            objs[obj_id]["cam_bbox_3d"] = bbox_coords.tolist()
            bbox_coords = camera2image_coords(bbox_coords, get_intrinsic_matrix(height, width, 90))
            # print(bbox_coords)

            min_point = np.min(bbox_coords, axis=0)
            max_point = np.max(bbox_coords, axis=0)

            bbox_2d = np.hstack((min_point, max_point))        # xyxy format
            # print(bbox_2d)
            objs[obj_id]["bbox_2d"] = bbox_2d.tolist()

        filtered_obj_list = select_obj_by_visible_bbox(objs, width, height, 0.8, 0.5)

        # visulize and save
        # img = cv2.imread(rgb_path)
        for obj in filtered_obj_list:
            bbox = obj["bbox_2d"]
            cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 0, 255), 3)
        # cv2.imshow(f"img", img)
        # cv2.waitKey()

        os.makedirs(os.path.join(obs_point_path, "visible_objs"), exist_ok=True)
        with open(os.path.join(obs_point_path, "visible_objs", f"{states[i]}"), "w", encoding="utf-8") as f:
            json.dump(objs, f, indent=4)
        print(f"{states[i]} saved")


def process_obs_point(obs_point_path, obj_info):
    if not os.path.exists(obs_point_path):
        raise FileNotFoundError(f"{obs_point_path} does not exist")

    states = os.listdir(os.path.join(obs_point_path, "state"))

    with open(os.path.join(obs_point_path, "state", states[0])) as f:
        state = json.load(f)
    ego_loc = np.array(state["translation"])

    selected_objs = select_obj_by_range(ego_loc, obj_info)
    project_bbox2view(selected_objs, obs_point_path)


def caption_processor(data_dir):
    obj_info_path = "../data/object_info.json"
    if not os.path.exists(obj_info_path):
        raise FileNotFoundError(f"{obj_info_path} does not exist")

    with open(obj_info_path, 'r') as f:
        obj_info = json.load(f)

    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"{data_dir} does not exist")

    data_seqs = os.listdir(data_dir)
    for idx, seq in enumerate(data_seqs):
        # if seq != '201':
        #     continue
        seq_path = os.path.join(data_dir, seq)
        print(seq_path)
        process_obs_point(seq_path, obj_info)


if __name__ == "__main__":
    caption_processor("../data/embodied_tasks_new_refine")
