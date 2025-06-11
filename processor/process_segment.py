import os
import sys
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  
sys.path.append(root_path)
import argparse
import numpy as np
import pandas as pd
from vqasynth.datasets.segment import CLIPSeg, SAM, sample_points_from_heatmap
import traceback

clipseg = CLIPSeg(model_path="vqasynth/models/clipseg")
sam = SAM(model_path="vqasynth/models/sam", device="cuda")

def segment_image_data(row):
    try:
        # print(row["image"].size)
        preds = clipseg.run_inference(row["image"], row["caption"]) 
        # print(preds.shape)
        sampled_points = [] 
        sam_masks = [] 

        original_size = row["image"].size
        # print(row['caption'], preds.shape)

        for idx in range(preds.shape[0]):

            sampled_points.append(sample_points_from_heatmap(preds[idx][0], original_size, num_points=10))     

        for idx in range(preds.shape[0]):
            mask_tensor = sam.run_inference_from_points(row["image"], [sampled_points[idx]], multimask_output=False)
            # mask = cv2.cvtColor(255 * mask_tensor[0].numpy().squeeze().transpose((1, 2, 0)).astype(np.uint8), cv2.COLOR_BGR2GRAY)
            mask = 255 * mask_tensor[0].numpy().squeeze().astype(np.uint8)
            sam_masks.append(mask)
        # print(row['caption'], sam_masks)

        return sam_masks
    except Exception as e:
        print(f"[Error] Failed to process row with caption: {row.get('caption', 'Unknown')}")
        traceback.print_exc() 
        return []


def main(output_dir):
    for filename in os.listdir(output_dir):
        if filename.endswith('.pkl'):
            pkl_path = os.path.join(output_dir, filename)
            # Load the DataFrame from the .pkl file
            df = pd.read_pickle(pkl_path)

            # Process each image and add the results to a new column
            df['masks'] = df.apply(segment_image_data, axis=1)

            # Save the updated DataFrame back to the .pkl file
            df.to_pickle(pkl_path)
            print(f"Processed and updated {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images from .pkl files", add_help=True)
    parser.add_argument("--output_dir", type=str, required=True, help="path to directory containing .pkl files")
    args = parser.parse_args()

    main(args.output_dir)
