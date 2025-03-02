import os
import sys
import json
import uuid
import numpy as np
sys.path.append("../")
from utils.bbox_utils import bbox_diagonal2vertice

def id_processor(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("File {} does not exist".format(file_path))

    with open(file_path, 'rb') as f:
        meta_data = json.load(f)
    print(meta_data)

    processed_data = {}
    for actor in meta_data:
        print(actor)
        actor_id = str(uuid.uuid4().hex)
        actor_name = actor

        bbox = meta_data[actor_name]
        p1 = bbox["p1"]
        p2 = bbox["p2"]

        p1 = np.array([p1['x'], p1['y'], p1['z']])
        p2 = np.array([p2['x'], p2['y'], p2['z']])
        actor_bbox_3d = bbox_diagonal2vertice(p1, p2)
        actor_loc = np.mean(actor_bbox_3d, axis=0)

        processed_data[actor_id] = {
            "actor_id": actor_id,
            "actor_name": actor_name,
            "actor_bbox_3d": actor_bbox_3d.tolist(),
            "actor_loc": actor_loc.tolist()
        }

    # print(processed_data)
    print(len(processed_data))
    with open(file_path.replace("BuildingBBox", "object_info"), 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, indent=4)


if __name__ == '__main__':
    id_processor('../data/BuildingBBox.json')

