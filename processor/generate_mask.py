import pickle
import matplotlib.pyplot as plt
import os
import numpy as np
import cv2
import argparse

def draw_bbox(rgb, mask, threshold=100, color=(255, 0, 0), thickness=3):
    rgb = np.array(rgb)

    mask_thresholded = np.where(mask > threshold, 255, 0).astype(np.uint8) 
    contours, _ = cv2.findContours(mask_thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    x_min, y_min, x_max, y_max = float('inf'), float('inf'), float('-inf'), float('-inf')

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x + w)
        y_max = max(y_max, y + h)

    rgb_copy = rgb.copy()
    cv2.rectangle(rgb_copy, (x_min, y_min), (x_max, y_max), color, thickness)
    
    return rgb_copy

def main(output_dir):
    font_size = 55

    chunk_path = os.path.join(output_dir, "chunk_0.pkl")

    with open(chunk_path, "rb") as f:
        data = pickle.load(f)

    save_dir = os.path.join(output_dir, "refine")
    os.makedirs(save_dir, exist_ok=True)
    for idx, row in data.iterrows():
        
        captions = data['caption'].values
        caption = captions[idx] 
        image_filename = data['image_filename'].values[idx] 
        masks = data.loc[idx, 'masks']
        rgb = data.loc[idx, 'image']

        if len(masks) == 3:
  
            fig, axes = plt.subplots(2, 3, figsize=(60, 30))

            axes[0, 0].imshow(draw_bbox(rgb, masks[0]))
            axes[0, 0].set_title(caption[0], fontsize=font_size)
            axes[0, 0].axis('off')

            axes[1, 0].imshow(masks[0])
            axes[1, 0].axis('off')

            axes[0, 1].imshow(draw_bbox(rgb, masks[1]))
            axes[0, 1].set_title(caption[1], fontsize=font_size)
            axes[0, 1].axis('off')

            axes[1, 1].imshow(masks[1])
            axes[1, 1].axis('off')

            axes[0, 2].imshow(draw_bbox(rgb, masks[2]))
            axes[0, 2].set_title(caption[2], fontsize=font_size)
            axes[0, 2].axis('off')

            axes[1, 2].imshow(masks[2])
            axes[1, 2].axis('off')


        elif len(masks) == 2:
            fig, axes = plt.subplots(2, 2, figsize=(60, 30))

            axes[0, 0].imshow(draw_bbox(rgb, masks[0]))
            axes[0, 0].set_title(caption[0], fontsize=font_size)
            axes[0, 0].axis('off')

            axes[1, 0].imshow(masks[0])
            axes[1, 0].axis('off')

            axes[0, 1].imshow(draw_bbox(rgb, masks[1]))
            axes[0, 1].set_title(caption[1], fontsize=font_size)
            axes[0, 1].axis('off')

            axes[1, 1].imshow(masks[1])
            axes[1, 1].axis('off')

        else:
            continue

        plt.subplots_adjust(wspace=0.3, hspace=0.05) 

        save_path = os.path.join(save_dir, f"{image_filename}")
        plt.savefig(save_path, dpi=200)

        plt.close(fig)  
        print(f"Saved {save_path}")
        # plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images from .pkl files", add_help=True)
    parser.add_argument("--output_dir", type=str, required=True, help="path to directory containing .pkl files")
    args = parser.parse_args()

    main(args.output_dir)