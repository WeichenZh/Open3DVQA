import json
import os
import pickle
import argparse
import pandas as pd
import io
import numpy as np
import PIL
from PIL import Image
from openai import OpenAI
import json
import base64


class Open3DVQA:
    def __init__(self):
        self.client = OpenAI(
            api_key="API-KEY",  # api key,
            api_version="2024-07-01-preview",
            azure_endpoint="end-point". # end point
        )

    def image_to_base64_data_uri(self, image_input):
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

    def query(self, question, image):
        image_uri = self.image_to_base64_data_uri(image)
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
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
        print(response.choices[0].message.content)
        resp = response.choices[0].message.content

        return resp


vqa_agent = Open3DVQA()

# 读取JSON文件
base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, '..', 'data', 'annotations', 'valid_qa.json')
with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

gpt_responses = []
# 遍历JSON数据
for item in data:
    item_id = item.get('id')
    image_info = item.get('image_info', {})
    qa_info = item.get('qa_info', {})
    conversation = item.get('conversation', [])

    image_path = os.path.join(base_dir, image_info['image_path'])
    depth_path = os.path.join(base_dir, image_info['depth_path'])

    # 检查图像路径是否存在
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # 检查深度路径是否存在
    if not os.path.exists(depth_path):
        raise FileNotFoundError(f"Depth file not found: {depth_path}")

    # 尝试打开图像文件
    try:
        image = PIL.Image.open(image_path)
    except Exception as e:
        raise IOError(f"Failed to open image file: {image_path}. Error: {e}")

    # 尝试加载深度文件
    try:
        depth_map = np.load(depth_path)
        depth_map = PIL.Image.fromarray(depth_map.squeeze())
    except Exception as e:
        raise IOError(f"Failed to load depth file: {depth_path}. Error: {e}")

    # 获取QA信息
    qa_type = qa_info.get('type')
    question_name = qa_info.get('question_name')

    # 获取对话内容
    if conversation:
        answer = conversation[1].get('value')
    else:
        answer =None

    question = item.get('query_question')

    resp = vqa_agent.query(question, image)

    gpt_response = {
        "id": item_id,
        "qa_info": qa_info,
        "question": question,
        "answer": answer,
        "response": response.choices[0].message.content
    }
    gpt_responses.append(gpt_response)

result_dir = os.path.join(base_dir, 'response_result', 'gpt-4', 'gpt_responses.json')
# 将列表保存为JSON文件
with open(result_dir, 'w', encoding='utf-8') as f:
    json.dump(gpt_responses, f, ensure_ascii=False, indent=4)
