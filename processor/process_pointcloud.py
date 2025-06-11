import json
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  
sys.path.append(root_path)
import open3d as o3d
import argparse
import numpy as np
import pandas as pd
from pathlib import Path

from scipy.spatial.transform import Rotation as R

from vqasynth.datasets.segment import apply_mask_to_image
from vqasynth.datasets.pointcloud import create_point_cloud_from_rgbd, save_pointcloud, canonicalize_point_cloud

def get_intrinsic(scene_name, width, height, fov):
    if scene_name == "EmbodiedCity" or scene_name == "UrbanScene":
        fov_x = np.radians(fov)
        fov_y = 2 * np.arctan((height * 1.0 / width) * np.tan(fov_x / 2))

        intrinsic_parameters = {
            'width': width,
            'height': height,
            'fx': width / (2 * np.tan(fov_x / 2)),  # 1.5 * width,
            'fy': height / (2 * np.tan(fov_y / 2)),  # 1.5 * width,
            'cx': width / 2,
            'cy': height / 2,
        }

    elif scene_name == "RealworldUAV":
        intrinsic_parameters = {
            'width': width,
            'height': height,
            'fx': 493.68,  # 1.5 * width,
            'fy': 491.56,  # 1.5 * width,
            'cx': 319.10,
            'cy': 189.21,
        }
    elif scene_name == "WildUAV":
        intrinsic_parameters = {
            'width': width,
            'height': height,
            'fx': 4548.91 / 8,
            'fy': 4548.91 / 8,
            'cx': 2647.23 / 8,
            'cy': 1964.00 / 8,
        }
    else:
        raise ValueError(f"Unknown scene name: {scene_name}")

    return intrinsic_parameters


def pointcloud_image_data(row, output_dir, use_gt=False):
    print(row["image_path"])
    original_image_cv = np.array(row["image"].convert('RGB'))
    depth_image_cv = np.repeat(np.array(row["depth_map"])[:, :, np.newaxis], 3, axis=2)

    if "EmbodiedCity" in row['image_path']:
        scene_name = "EmbodiedCity"
    elif "UrbanScene" in row['image_path']:
        scene_name = "UrbanScene"
    elif "RealworldUAV" in row['image_path']:
        scene_name = "RealworldUAV"
    elif "WildUAV" in row['image_path']:
        scene_name = "WildUAV"
    else:
        raise ValueError(f"Unknown scene name: {row['image_path']}")

    if use_gt:
        width, height = row["image"].size
        fov = 90
        intrinsic_parameters = get_intrinsic(scene_name, width, height, fov)
        camera_pose_file = row["image_path"].replace('rgb', 'pose')[:-4] + '.json'
        # construct extrinsic matrix
        with open(camera_pose_file, 'r') as f:
            camera_pose = json.load(f)

        # obtain roll, pitch, yaww
        qw, qx, qy, qz = camera_pose['rotation']
        r = R.from_quat([qx, qy, qz, qw])
        if scene_name == "EmbodiedCity" or scene_name == "UrbanScene":
            # construct canonicalized extrinsic matrix, rotate y, -pitch degrees
            roll, pitch, yaw = r.as_euler("xyz", degrees=True)
            r_tar = R.from_euler('y', -pitch, degrees=True).as_matrix()
            r_diff = r_tar
        elif scene_name == "RealworldUAV":
            # construct canonicalized extrinsic matrix, rotate y, -pitch degrees
            roll, pitch, yaw = r.as_euler("xyz", degrees=True)
            r_tar = R.from_euler('y', pitch, degrees=True).as_matrix()
            r_diff = r_tar
        elif scene_name == "WildUAV":
            yaw, roll, pitch = r.as_euler("xyz", degrees=True)
            print(pitch)
            if pitch < 0:
                pitch = 180 + pitch
            r_tar = R.from_euler('y', pitch, degrees=True).as_matrix()
            r_diff = r_tar
    else:
        #  todo: load estimated camera intrinsic
        pass

    point_clouds = []
    point_cloud_data = []

    for i, mask in enumerate(row["masks"]):
        mask_binary = mask > 0

        masked_rgb = apply_mask_to_image(original_image_cv, mask_binary)
        masked_depth = apply_mask_to_image(depth_image_cv, mask_binary)

        # 1. project to camera
        pcd = create_point_cloud_from_rgbd(masked_rgb, masked_depth, intrinsic_parameters)

        # 2. canonicalize, remove pitch, roll
        # 2.1 convert to airsim ego coordinate system, because rotation matrix is originally designed for airsim coordinate systems
        pcd_cam = np.array(pcd.points)
        pcd_ego = np.stack([pcd_cam[:, 2], -pcd_cam[:, 0], -pcd_cam[:, 1]], axis=-1)

        pcd.points = o3d.utility.Vector3dVector(pcd_ego)
        print("before rotate:", np.array(pcd.points).mean(axis=0))
        # o3d.visualization.draw_geometries([pcd])

        # 2.2 rotate to canonicalized coordinate system
        pcd.rotate(r_diff, center=(0, 0, 0))
        print("after rotate:", np.array(pcd.points).mean(axis=0))
        # o3d.visualization.draw_geometries([pcd])

        point_clouds.append(pcd)

    # vis global point cloud
    pcd_all = create_point_cloud_from_rgbd(original_image_cv, depth_image_cv, intrinsic_parameters)
    pcd_cam = np.array(pcd_all.points)
    pcd_cam = np.stack([pcd_cam[:, 2], -pcd_cam[:, 0], -pcd_cam[:, 1]], axis=-1)
    pcd_all.points = o3d.utility.Vector3dVector(pcd_cam)
    pcd_all.rotate(r_diff, center=(0, 0, 0))
    # o3d.visualization.draw_geometries([pcd_all])

    # print(len(point_clouds), row['caption'], len(row['masks']))
    valid_idx = [True] * len(point_clouds)
    for idx, pcd in enumerate(point_clouds):
        pc_valid = True
        cl, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
        inlier_cloud = pcd.select_by_index(ind)
        if len(inlier_cloud.points) < 100:          # less than 100 points, not valid
            pc_valid = False

        pointcloud_filepath = os.path.join(output_dir, "pointclouds", f"pointcloud_{Path(row['image_filename']).stem}_{idx}_v2.pcd")

        if pc_valid:
            save_pointcloud(inlier_cloud, pointcloud_filepath)
            point_cloud_data.append(pointcloud_filepath)
        else:
            valid_idx[idx] = False
            point_cloud_data.append("")

        # o3d.visualization.draw_geometries([pcd])

    # Now, return both point_cloud_data and the canonicalized flag
    return point_cloud_data, None, valid_idx


def main(output_dir, use_gt=False):
    if use_gt:
        print("Using ground truth in point cloud process module.")

    point_cloud_dir = os.path.join(output_dir, "pointclouds")
    if not os.path.exists(point_cloud_dir):
        os.makedirs(point_cloud_dir)

    for filename in os.listdir(output_dir):
        if filename.endswith('.pkl'):
            pkl_path = os.path.join(output_dir, filename)
            df = pd.read_pickle(pkl_path)

            # Initialize empty lists to hold the pointclouds and canonicalization flags
            pointclouds = []
            is_canonicalized = []
            valid_idxes = []

            # Update to process each row and append results to lists
            for index, row in df.iterrows():
                pcd_data, canonicalized, valid_idx = pointcloud_image_data(row, output_dir, use_gt)
                # print(len(pcd_data), valid_idx)
                assert len(pcd_data) == len(valid_idx)
                pointclouds.append(pcd_data)
                is_canonicalized.append(canonicalized)
                valid_idxes.append(valid_idx)
            # Assign lists to new DataFrame columns
            df['pointclouds'] = pointclouds
            df['is_canonicalized'] = is_canonicalized
            df['valid_idx'] = valid_idxes

            df.to_pickle(pkl_path)
            print(f"Processed and updated {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images from .pkl files", add_help=True)
    parser.add_argument("--output_dir", type=str, required=True, help="path to directory containing .pkl files")
    parser.add_argument("--use_gt", action='store_true', help="use the gt point cloud and camera parameters")
    args = parser.parse_args()

    main(args.output_dir, args.use_gt)