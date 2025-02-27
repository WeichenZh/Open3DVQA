import os.path
import numpy as np
import json
import random
import argparse

def split_dataset(args):
    data_root = args.root_folder
    save_root = args.output_file
    with open(os.path.join(data_root, "merged.json")) as f:
        all_meta_data = json.load(f)

    scene_data = {}
    for meta_data in all_meta_data:
        for qa in meta_data:
            scene_id = qa["image_info"]["image_path"].split("\\")[-3]
            scene_id = int(scene_id)
            qa["scene_id"] = scene_id
            if scene_id not in scene_data:
                scene_data[scene_id] = []
            scene_data[scene_id].append(qa)

    scene_ids = list(scene_data.keys())
    random.shuffle(scene_ids)
    print(f"scene_ids: {len(scene_ids)}")
    for scene_id in scene_ids:
        print(f"Scene ID {scene_id}: {len(scene_data[scene_id])} items")
    train_split = int(len(scene_ids) * 0.8)
    valid_split = int(len(scene_ids) * 0.1)
    test_split = len(scene_ids) - train_split - valid_split

    train_scene_ids = scene_ids[:train_split]
    valid_scene_ids = scene_ids[train_split:train_split + valid_split]
    test_scene_ids = scene_ids[train_split + valid_split:]

    qa_splits = {"train": [], "valid": [], "test": []}

    for scene_id in train_scene_ids:
        qa_splits["train"].extend(scene_data[scene_id])
    for scene_id in valid_scene_ids:
        qa_splits["valid"].extend(scene_data[scene_id])
    for scene_id in test_scene_ids:
        qa_splits["test"].extend(scene_data[scene_id])

    print(f"train samples: {len(qa_splits['train'])}, valid samples: {len(qa_splits['valid'])}, test samples: {len(qa_splits['test'])}")

    with open(os.path.join(save_root, "train_qa.json"), "w") as f:
        json.dump(qa_splits["train"], f, indent=4)
    with open(os.path.join(save_root, "valid_qa.json"), "w") as f:
        json.dump(qa_splits["valid"], f, indent=4)
    with open(os.path.join(save_root, "test_qa.json"), "w") as f:
        json.dump(qa_splits["test"], f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-folder", type=str, required=True, help="path to root directory")
    parser.add_argument("--output-file", type=str, required=True, help="path to output JSON file")
    args = parser.parse_args()
    split_dataset(args)