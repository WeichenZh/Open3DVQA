import json
import os
from collections import defaultdict
from tqdm import tqdm
import io
import PIL
from PIL import Image
from openai import OpenAI
import json
import base64

def image_to_base64_data_uri(image_input):
    # Check if the input is a PIL Image
    if isinstance(image_input, Image.Image):
        buffer = io.BytesIO()
        image_input.save(buffer, format="PNG")  # You can change the format if needed
        base64_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

    else:
        raise ValueError("Unsupported input type. Input must be a file path or a PIL.Image.Image instance.")

    return f"data:image/png;base64,{base64_data}"

def count_qa(obj):
    count = 0
    if isinstance(obj, dict):
        if 'id' in obj:
            count += 1
        for value in obj.values():
            count += count_qa(value)
    elif isinstance(obj, list):
        for item in obj:
            count += count_qa(item)
    return count

def main():
    # read JSON data
    data_dir = "O3DVQA"
    result_dir = "response_result"
    json_path = os.path.join(data_dir, 'test_qa.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://api.openai.com/v1"  # default OpenAI API endpoint
    )
    
    model_name = "gpt-4o"

    responses = defaultdict(lambda: defaultdict(list))
    # with open(f'response_result/{model_name}_responses.json', 'r', encoding='utf-8') as f:
    #     resume_data = json.load(f)
    # for dataset, scenes in resume_data.items():
    #     for scene, scene_responses in scenes.items():
    #         for response in scene_responses:
    #             responses[dataset][scene].append(response)
    
    total_number = count_qa(data)
    progress_bar = tqdm(total=total_number, desc="Processing")
    # resume_flag = False

    for dataset, scenes in data.items():
        for scene, entries in scenes.items():
            for idx, item in enumerate(entries):
                item_id = item.get('id')
                # if item_id == "2290e7e8-dea7-4fdd-82e3-5606122b0546":
                #     resume_flag = True
                #     continue
                # if not resume_flag:
                #     progress_bar.update(1)
                #     continue
                file_name = item.get('image_name')
                # image_info = item.get('image_info', {})
                qa_info = item.get('qa_info', {})
                conversation = item.get('conversation', [])

                image_path = os.path.join(data_dir, dataset, scene, item.get('image_info').get('image_path'))

                if not os.path.exists(image_path):
                    raise FileNotFoundError(f"Image file not found: {image_path}")

                try:
                    image = PIL.Image.open(image_path)
                except Exception as e:
                    raise IOError(f"Failed to open image file: {image_path}. Error: {e}")
                
                if conversation:
                    answer = conversation[1].get('value')
                
                question = item.get('query_question')

                image_uri = image_to_base64_data_uri(image)
                max_retries = 10
                retry_count = 0
                while retry_count < max_retries:
                    try:
                        response = client.chat.completions.create(
                            timeout=90,
                            model=model_name,
                            messages=[
                                {
                                    "role": "system",
                                    "content": "You are an assistant who perfectly answer question in urban environment. Only based on the image, you should directly answer the height, width, volume and distance question with exact number Answer the distance without output intermediate process. You should answer the direction question in the direction of the clock with taking your front as 12 o 'clock, your left as 9 o 'clock, and your right as 3 o 'clock."
                                },
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "image_url",
                                            "image_url": {"url": image_uri}
                                        },
                                        {"type": "text",
                                            "text": question
                                        }
                                    ]
                                }
                            ]
                        )
                        break
                    except Exception as e:
                        print(f"Error during API call: {e}")
                        retry_count += 1
                else:
                    print("max retries exceeded, failed to API call.")

                response = {
                    "id": item_id,
                    "image_name": file_name,
                    "qa_info": qa_info,
                    "question": question,
                    "answer": answer,
                    "response": response.choices[0].message.content
                }
                responses[dataset][scene].append(response)

                progress_bar.update(1)

                if (idx+1) % 5 == 0:
                    # save per 5 responses
                    result_path = os.path.join(result_dir, f'{model_name}_responses.json')
                    os.makedirs(os.path.dirname(result_path), exist_ok=True)
                    with open(result_path, 'w', encoding='utf-8') as f:
                        json.dump({k: dict(v) for k, v in responses.items()}, f, ensure_ascii=False, indent=4)

            result_path = os.path.join(result_dir, f'{model_name}_responses.json')
            os.makedirs(os.path.dirname(result_path), exist_ok=True)
            with open(result_path, 'w', encoding='utf-8') as f:
                json.dump({k: dict(v) for k, v in responses.items()}, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
