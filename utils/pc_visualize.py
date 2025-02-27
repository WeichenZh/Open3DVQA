import open3d as o3d
import json
import numpy as np

def visualize_pc():
    pc_file = "E:\\ZWC\\traffic-simulation-5.3-beijing\\PointCloud.json"
    with open(pc_file, 'rb') as f:
        data = json.load(f)
    for k in data:
        raw_pc = data[k]
        break
    pc = []
    for p in raw_pc:
        pc.append([float(p['x']), float(p['y']), float(p['z'])])
    pc = np.array(pc)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pc)


    o3d.visualization.draw_geometries([pcd], window_name="pc show", width=1200, height=900)

if __name__ == '__main__':
    visualize_pc()

