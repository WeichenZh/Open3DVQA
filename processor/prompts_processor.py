import os
import cv2
import json
import pickle
import random
import itertools
import argparse
import numpy as np
import pandas as pd
from PIL import Image
from uuid import uuid4
from utils.prompts_utils import evaluate_predicates_on_pairs

def get_subfolders(folder):
    return [os.path.join(folder, subfolder) for subfolder in os.listdir(folder) if
            os.path.isdir(os.path.join(folder, subfolder))]
  # Replace with the actual folder path


def main(args):
    main_folder_path = args.main_folder_path  # Replace with the actual folder path
    subfolders = get_subfolders(main_folder_path)

    for subfolder in subfolders:
        images_path = os.path.join(subfolder, "rgb")
        bbox_images_path = os.path.join(subfolder, "cropped_images")
        objs_visible_path = os.path.join(subfolder, "visible_objs")
        # Skip if necessary folders do not exist
        if not os.path.exists(images_path) or not os.path.exists(objs_visible_path):
            print(f"Subfolder {subfolder} is missing 'rgb' or 'visible_objs' folder, skipping")

        images_samples = []

        # Traverse images in the rgb folder
        for image_filename in os.listdir(images_path):
            if image_filename.endswith(".png") or image_filename.endswith(".jpg"):
                image_path = os.path.join(images_path, image_filename)

                # JSON file path
                json_filename = os.path.splitext(image_filename)[0] + ".json"
                json_path = os.path.join(objs_visible_path, json_filename)

                # Check if JSON file exists
                if not os.path.exists(json_path):
                    print(f"JSON file {json_filename} does not exist in {objs_visible_path}, skipping this image")
                    continue

                # Read JSON file and get the objects
                with open(json_path, "r", encoding="utf-8") as json_file:
                    try:
                        data = json.load(json_file)
                    except json.JSONDecodeError:
                        print(f"Unable to parse JSON file: {json_filename}")
                        continue

                objects = []
                # Traverse each object in the JSON data to find bbox_2d
                for key, obj in data.items():
                    if "cropped_image_info" in obj:
                        objects.append(obj)
                    else:
                        continue

                try:
                    # Generate pairs of objects in order
                    all_pairs = [(i, j) for i in range(len(objects)) for j in range(i + 1, len(objects))]
                    # Randomly select some pairs to swap
                    num_to_swap = len(all_pairs) // 2  # Number of pairs to swap, can be adjusted as needed
                    pairs_to_swap = random.sample(all_pairs, num_to_swap)  # Randomly select pairs to swap
                    # Swap order
                    swapped_pairs = [(j, i) if (i, j) in pairs_to_swap else (i, j) for i, j in all_pairs]
                    # Randomly select two pairs and map back to original objects
                    random.shuffle(swapped_pairs)
                    selected_pairs = swapped_pairs
                    object_pairs = [(objects[i], objects[j]) for i, j in selected_pairs]
                    prompts, qa_info = evaluate_predicates_on_pairs(object_pairs)
                except Exception as e:
                    print(e)
                    prompts = []
                    qa_info = []

                if prompts and qa_info:
                    conversations = []
                    first_prompt = True
                    if len(prompts) != len(qa_info):
                        raise ValueError("The lengths of the lists are not the same!")
                    # Assume prompts and row['qa_information'] have the same length
                    for prompt, question_name in zip(prompts, qa_info):
                        conversation = []
                        qa_information = {}
                        # Process prompts
                        if 'Answer: ' in prompt:
                            question, answer = prompt.split('Answer: ', 1)
                            # human_value = f"<image>\n{question}" if first_prompt else question
                            human_value = f"<image>\n{question}"
                            conversation.append({
                                "from": "human",
                                "value": human_value
                            })
                            conversation.append({
                                "from": "gpt",
                                "value": answer
                            })
                            first_prompt = False

                        # Process qa_information
                        if 'choice' in question_name or 'predicate' in question_name or 'relationship' in question_name:
                            qa_information = {
                                "type": 'qualitative',
                                "question_name": question_name
                            }
                        elif 'data' in question_name or 'distance' in question_name or 'direction2agent' in question_name:
                            qa_information = {
                                "type": 'quantitative',
                                "question_name": question_name
                            }
                        if 'agent' in question_name:
                            qa_information["is_embodied"] = True
                        else:
                            qa_information["is_embodied"] = False

                        image_path = os.path.join(images_path, image_filename)
                        depth_file_path = image_path.replace('RGBVis', 'Depth').replace('rgb', 'depth').replace('.png',
                                                                                                                '.npy')
                        image_info = {
                            "image_path": image_path,
                            "depth_path": depth_file_path
                        }
                        obj_ids = []
                        for obj in object_pairs:
                            obj_ids += [obj[0]['actor_id'], obj[1]['actor_id']]
                        obj_ids = list(set(obj_ids))
                        image_sample = {
                            # "id": image_filename + '_' + question_name,
                            "id": str(uuid4().hex),
                            # Ensure the image path format fits your structure
                            "object_id": obj_ids,
                            "image_info": image_info,
                            "qa_info": qa_information,
                            "conversation": conversation,
                            "query_question": question
                        }
                        images_samples.append(image_sample)

        # Save the final samples to the output JSON file
        vqa_data_json = os.path.join(subfolder, "vqa_dataset.json")
        with open(vqa_data_json, "w") as json_file:
            json.dump(images_samples, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--main-folder-path", type=str, required=True, help="path to main directory")
    args = parser.parse_args()
    main(args)