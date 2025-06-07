import os
import pickle
import argparse
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import PIL.Image
import pandas as pd
import numpy as np
from vqasynth.wrappers.zoedepth import ZoeDepth

zoe_depth = ZoeDepth()

def get_image_depth(image_path, use_gt=False):
    if use_gt:
        depth_file_path = image_path.replace('RGBVis', 'Depth').replace('rgb', 'depth').replace('.png', '.npy').replace('.jpg', '.npy')
        depth_map = np.load(depth_file_path)
        depth_map = PIL.Image.fromarray(depth_map.squeeze())
    else:
        rgb_img = PIL.Image.open(image_path)
        depth_map = zoe_depth.infer_direct_depth(rgb_img)
    # print(depth_map.size)
    return depth_map


def main(output_dir, use_gt=False):
    for filename in os.listdir(output_dir):
        if filename.endswith('.pkl'):
            pkl_path = os.path.join(output_dir, filename)
            # Load the DataFrame from the .pkl file
            df = pd.read_pickle(pkl_path)
            # Process each image and add the results to a new column
            df['depth_map'] = df['image_path'].apply(get_image_depth, args=use_gt)

            # Save the updated DataFrame back to the .pkl file
            df.to_pickle(pkl_path)
            print(f"Processed and updated {filename}")


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Process images from .pkl files", add_help=True)
    parser.add_argument("--output_dir", type=str, required=True, help="path to directory containing .pkl files")
    args = parser.parse_args()

    main(args.output_dir)

