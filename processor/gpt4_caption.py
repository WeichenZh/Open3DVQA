import os
import pickle
import argparse
import pandas as pd
import openai
import io
from PIL import Image, ImageDraw
from openai import OpenAI
import json
import base64

def image_to_base64_data_uri(image_input):
    # Check if the input is a file path (string)
    if isinstance(image_input, str):
        with open(image_input, "rb") as img_file:
            base64_data = base64.b64encode(img_file.read()).decode('utf-8')

    # Check if the input is a PIL Image
    elif isinstance(image_input, Image.Image):
        buffer = io.BytesIO()
        image_input.save(buffer, format="PNG")  # You can change the format if needed
        base64_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

    else:
        raise ValueError("Unsupported input type. Input must be a file path or a PIL.Image.Image instance.")

    return f"data:image/png;base64,{base64_data}"

client = OpenAI(
    api_key='',
    base_url=""
)

def generate_image_description(image):
    data_uri = image_to_base64_data_uri(image)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant who perfectly describes images in urban environment, considering all your knowledge of urban environment."
            },
            {
                "role": "user",
                "content": [
                    {"type": "image_url",
                     "image_url": {"url": data_uri}
                     },
                    {"type": "text",
                         "text": 'Create a description about the main, distinct object in the bounding box with concise, up to eight-word. Highlight its color, appearance, style, shape, structure, material. Do not return content with a period.'
                     }
                ]
            }
        ],
        # temperature=0.2,
        # response_format={"type": "json_object"}
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def get_subfolders(folder):
    return [os.path.join(folder, subfolder) for subfolder in os.listdir(folder) if
            os.path.isdir(os.path.join(folder, subfolder))]

def is_bbox_within_image(bbox, image_width, image_height):
    x_min, y_min, x_max, y_max = bbox
    return (
        0 <= x_min < image_width and
        0 <= y_min < image_height and
        0 < x_max <= image_width and
        0 < y_max <= image_height
    )

def main(args):
    # Set minimum width and height
    min_width = 30  # Minimum width
    min_height = 30  # Minimum height

    main_folder_path = args.main_folder_path  # Replace with the actual folder path
    subfolders = get_subfolders(main_folder_path)

    for subfolder in subfolders:
        images_path = os.path.join(subfolder, "rgb")
        bbox_images_path = os.path.join(subfolder, "cropped_images")
        objs_visible_path = os.path.join(subfolder, "visible_objs")

        # Skip if necessary folders do not exist
        if not os.path.exists(images_path) or not os.path.exists(objs_visible_path):
            print(f"Subfolder {subfolder} is missing 'rgb' or 'visible_objs' folder, skipping")
            continue

        # Create cropped_images folder
        os.makedirs(bbox_images_path, exist_ok=True)

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

                # Read JSON file and get the values of bbox_2d key for all objects
                with open(json_path, "r", encoding="utf-8") as json_file:
                    try:
                        data = json.load(json_file)
                    except json.JSONDecodeError:
                        print(f"Unable to parse JSON file: {json_filename}")
                        continue

                # Extract bbox and crop, save images
                with Image.open(image_path) as img:
                    image_width, image_height = img.size

                    # Traverse each object in the JSON data to find bbox_2d
                    for obj_key, obj in data.items():
                        bbox = obj.get("bbox_2d")
                        if bbox and is_bbox_within_image(bbox, image_width, image_height):
                            x_min, y_min, x_max, y_max = bbox

                            # Calculate the width and height of the box
                            width = x_max - x_min
                            height = y_max - y_min

                            # Check if the width and height of the box exceed the minimum threshold
                            if width >= min_width and height >= min_height:
                                # Crop and save the image
                                cropped_img = img.crop((x_min, y_min, x_max, y_max))
                                cropped_image_name = f"{os.path.splitext(image_filename)[0]}_crop_{obj_key}.png"
                                cropped_image_path = os.path.join(bbox_images_path, cropped_image_name)
                                cropped_img.save(cropped_image_path)

                                cropped_img_caption = generate_image_description(cropped_img)
                                # Store the cropped image path information in the JSON data
                                data[obj_key]["cropped_image_info"] = {
                                    "cropped_image_path": cropped_image_path,
                                    "cropped_image_caption": cropped_img_caption
                                }
                            else:
                                continue

                # Write the updated JSON data back to the original file
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)

                print(f"Cropped image information has been added to {json_path}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--main-folder-path", type=str, required=True, help="path to main directory")
    args = parser.parse_args()
    main(args)