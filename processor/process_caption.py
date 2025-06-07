import os
import pickle
import argparse
import pandas as pd
import io
from PIL import Image
from openai import AzureOpenAI
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

def extract_descriptions_from_incomplete_json(json_like_str):
    last_object_idx = json_like_str.rfind(',"object')
    
    if last_object_idx != -1:
        json_str = json_like_str[:last_object_idx] + '}'
    else:
        json_str = json_like_str.strip()
        if not json_str.endswith('}'):
            json_str += '}'
    
    try:
        json_obj = json.loads(json_str)
        descriptions = [details['description'].replace(".","") for key, details in json_obj.items() if 'description' in details]

        return descriptions
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON: {e}")

def caption_image_data(image):
    client = AzureOpenAI(
        api_key="",  
        api_version="",
        azure_endpoint=""
        # end point
    )
    data_uri = image_to_base64_data_uri(image)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant who perfectly describes images."
            },
            {
                "role": "user",
                "content": [
                    {"type": "image_url",
                     "image_url": {"url": data_uri}
                    },
                    {"type": "text",
                     "text": 'Create a JSON representation where each entry consists of a key "object" with a numerical suffix starting from 1, and a corresponding "description" key. The description should be a concise sentence (max six words) identifying one visually distinctive object or building in the image. Only describe up to three unique objects that clearly differ in color, shape, or category. Do not include background elements like sky or ground. Avoid duplicates. If no qualifying objects are present, return an empty JSON {}. An example: {"object1": { "description": "Man in red hat walking." },"object2": { "description": "Wooden pallet with boxes." },"object3": { "description": "Cardboard boxes stacked." }}'
                    }
                ]
            }
        ],
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content


def process_images_in_chunks(image_dir, chunk_size=100):
    """Generator function to yield chunks of images from the directory."""
    chunk = []
    for image_filename in os.listdir(image_dir):
        if image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            chunk.append(image_filename)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
    if chunk:
        yield chunk


def main(image_dir, output_dir, use_gt=False):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    chunk_index = 0

    for chunk in process_images_in_chunks(image_dir):
        print("Processing chunk ", chunk_index)
        records = []

        for image_filename in chunk:
            if 'down_90' in image_filename:
                continue
            image_path = os.path.join(image_dir, image_filename)

            try:
                img = Image.open(image_path).convert('RGB')
                if use_gt:
                    caption = []
                else:
                    caption = caption_image_data(image_path)
                desrpition = extract_descriptions_from_incomplete_json(caption)
                print(desrpition)
                records.append({
                    "image_filename": image_filename,
                    "image_path": image_path,
                    "image": img,
                    "caption": desrpition
                })
            except Exception as e:
                print(f"Error processing {image_path}: {e}")

        # Convert records to a pandas DataFrame
        df = pd.DataFrame(records)

        # Save the DataFrame to a .pkl file
        output_filepath = os.path.join(output_dir, f"chunk_{chunk_index}.pkl")
        df.to_pickle(output_filepath)

        print(f"Processed chunk {chunk_index} with {len(chunk)} images.")
        chunk_index += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images and generate captions", add_help=True)
    parser.add_argument("--image_dir", type=str, required=True, help="path to directory containing image files")
    parser.add_argument("--output_dir", type=str, required=True, help="path to directory to save .pkl files")
    parser.add_argument("--use_gt", type=bool, default=False, help="use the gt caption")
    args = parser.parse_args()

    main(args.image_dir, args.output_dir, args.use_gt)
