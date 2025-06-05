import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import cv2
import json
import pickle
import random
import itertools
import argparse
import numpy as np
import pandas as pd
from vqasynth.datasets.pointcloud import restore_pointclouds
from vqasynth.datasets.prompts import evaluate_predicates_on_pairs


def prompt_image_data(row):
    image_file = row["image_filename"]
    captions = row["caption"]
    pointcloud_path = row["pointclouds"]
    is_canonicalized = row["is_canonicalized"]
    valid_idx = row["valid_idx"]
    # print(valid_idx, captions)

    captions = [captions[i] for i in range(len(captions)) if valid_idx[i]]
    pointcloud_path = [pointcloud_path[i] for i in range(len(pointcloud_path)) if valid_idx[i]]

    pointclouds = restore_pointclouds(pointcloud_path)

    try:
        objects = list(zip(captions, pointclouds))
        all_pairs = [(i, j) for i in range(len(objects)) for j in range(len(objects)) if i != j]
        random.shuffle(all_pairs)
        selected_pairs = all_pairs[:2]
        object_pairs = [(objects[i], objects[j]) for i,j in selected_pairs]
        prompts, qa_information = evaluate_predicates_on_pairs(object_pairs, is_canonicalized)
        
    except Exception as e:
        print(e)
        prompts = []
        qa_information = []
    return prompts, qa_information


def main(image_dir, output_dir):
    final_samples = []
    images_samples = []
    for filename in os.listdir(output_dir):
        if filename.endswith('.pkl'):
            pkl_path = os.path.join(output_dir, filename)
            # Load the DataFrame from the .pkl file
            df = pd.read_pickle(pkl_path)

            # Process each image and add the results to a new column
            # df['prompts'] = df.apply(prompt_image_data, axis=1)
            df[['prompts', 'qa_information']] = df.apply(lambda row: pd.Series(prompt_image_data(row)), axis=1)
            # Save the updated DataFrame back to the .pkl file
            df.to_pickle(pkl_path)
            print(f"Processed and updated {filename}")

            for index, row in df.iterrows():
                # Check if the image filename is valid
                if row['prompts'] and any(row['prompts']):
                    image_filename = row['image_filename']
                    conversations = []
                    first_prompt = True
                    for prompt in row['prompts']:
                        if 'Answer: ' in prompt:
                            question, answer = prompt.split('Answer: ', 1)
                            human_value = f"<image>\n{question}" if first_prompt else question
                            conversations.append({
                                "from": "human",
                                "value": human_value
                            })
                            conversations.append({
                                "from": "gpt",
                                "value": answer
                            })
                            first_prompt = False

                    if conversations:  # Ensure we have valid conversation data
                        sample = {
                            "id": image_filename,
                            # Ensure the image path format fits your structure
                            "image": os.path.join(image_dir, image_filename),
                            "conversations": conversations
                        }
                        final_samples.append(sample)

                if row['prompts'] and any(row['prompts']) and row['qa_information'] and any(row['qa_information']):
                    image_filename = row['image_filename']
                    conversations = []
                    first_prompt = True
                    if len(row['prompts']) != len(row['qa_information']):
                        raise ValueError("列表的长度不相同！")
                    # 假设 row['prompts'] 和 row['qa_information'] 的长度相同
                    for prompt, question_name in zip(row['prompts'], row['qa_information']):
                        print(row['qa_information'])
                        conversation = []
                        qa_information = {}
                        # 处理 prompts
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

                        # 处理 qa_information
                        if 'choice' in question_name or 'predicate' in question_name or 'relationship' in question_name:
                            qa_information={
                                "type": 'qualitative',
                                "question_name": question_name
                            }
                        elif 'data' in question_name or 'distance' in question_name or 'direction2agent' in question_name:
                            qa_information={
                                "type": 'quantitative',
                                "question_name": question_name
                            }
                        if 'agent' in question_name:
                            qa_information["is_embodied"] = True
                        else:
                            qa_information["is_embodied"] = False

                        image_path = os.path.join(image_dir, image_filename)
                        depth_file_path = image_path.replace('RGBVis', 'Depth').replace('rgb', 'depth').replace('.png', '.npy').replace('.jpg', '.npy')
                        image_info = {
                            "image_path": image_path,
                            "depth_path": depth_file_path
                        }
                        image_sample = {
                            "id": image_filename + '_' + question_name,
                            # Ensure the image path format fits your structure
                            "image_info": image_info,
                            "qa_info": qa_information,
                            "conversation": conversation,
                            "query_question": question
                        }
                        images_samples.append(image_sample)


    # Save the final samples to the output JSON file
    output_json = os.path.join(output_dir, "processed_dataset.json")
    with open(output_json, "w") as json_file:
        json.dump(final_samples, json_file, indent=4)

    test_json = os.path.join(output_dir, "test_dataset.json")
    with open(test_json, "w") as json_file:
        json.dump(images_samples, json_file, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images from .pkl files", add_help=True)
    parser.add_argument("--image_dir", type=str, required=True, help="path to image directory")
    parser.add_argument("--output_dir", type=str, required=True, help="path to directory containing .pkl files")
    args = parser.parse_args()

    main(args.image_dir, args.output_dir)
