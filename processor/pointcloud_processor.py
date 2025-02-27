import json

import open3d as o3d
import numpy as np


def visualize_pointcloud(pc):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pc)
    o3d.visualization.draw_geometries([pcd])


if __name__ == '__main__':
    pc_file_path = "E:\\Open3DVQA\\data\\PointCloud.json"
    obj_info_path = "E:\\Open3DVQA\\data\\object_info.json"
    obj_ids = [
        "4fb24a4c9f0e46e1897dc116ebe678a0",
        "f7eb5cff1ff34161bd4b8120e053120d",
        "9b156ceaa90546cab39ca56a701cb0a8",
        "fbd8d49db8aa4e7bb32e3f6ef52d95e5"
    ]
    with open(obj_info_path, "r", encoding="utf-8") as f:
        obj_info = json.load(f)

    with open(pc_file_path, 'rb') as f:
        pc_info = json.load(f)

    actor_names = [obj_info[obj_id]["actor_name"] for obj_id in obj_ids]
    print(actor_names)
    print(pc_info.keys())
    pcs = []
    for actor_name in actor_names:
        raw_pc = pc_info[actor_name]
        # print(len(raw_pc))
        pc = []
        for p in raw_pc:
            pc.append([p['x'], p['y'], p['z']])
        pc = np.array(pc)
        pcs.append(pc)
        visualize_pointcloud(np.array(pc))
        # print(pc)
        print(len(pc))
    print(len(pcs))

