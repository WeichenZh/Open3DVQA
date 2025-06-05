import json
from openai import OpenAI
import os
import base64
import dashscope
from dashscope import MultiModalConversation

# llava v1.6
from llama_cpp import Llama
from llama_cpp.llama_chat_format import Llava15ChatHandler

from vqasynth.datasets.utils import image_to_base64_data_uri

# GPT-4o
import openai

class Llava:
    def __init__(self, mmproj="/app/models/mmproj-model-f16.gguf", 
                 model_path="/app/models/llava-v1.6-34b.Q4_K_M.gguf", gpu=True):
        chat_handler = Llava15ChatHandler(clip_model_path=mmproj, verbose=True)
        # chat_handler = Llava15ChatHandler(clip_model_path=mmproj)
        n_gpu_layers = -1
        if gpu:
           n_gpu_layers = 30
        self.llm = Llama(model_path=model_path, chat_handler=chat_handler, n_ctx=2048, logits_all=True, n_gpu_layers=n_gpu_layers)

    def run_inference(self, image, prompt, return_json=True):
        data_uri = image_to_base64_data_uri(image)
        res = self.llm.create_chat_completion(
             messages = [
                 {"role": "system", "content": "You are an assistant who perfectly describes images."},
                 {
                     "role": "user",
                     "content": [
                         {"type": "image_url", "image_url": {"url": data_uri}},
                         {"type" : "text", "text": prompt}
                    ]
                 }
               ]
             )
        if return_json:
            return list(set(self.extract_descriptions_from_incomplete_json(res["choices"][0]["message"]["content"])))
        return res["choices"][0]["message"]["content"]

    def extract_descriptions_from_incomplete_json(self, json_like_str):
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

    
class Qwen:
    def __init__(self, api_key, base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", model="qwen-vl-plus"):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

    def run_inference(self, image, prompt, return_json=True):
        data_uri = image_to_base64_data_uri(image)
        client = OpenAI(
            api_key=self.api_key,   
            base_url=self.base_url,
        )
        messages = [
                {"role": "system", "content": "You are an assistant who perfectly describes images."},
                {
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": data_uri}},
                        {"type" : "text", "text": 'Create a JSON representation where each entry consists of a key "object" with a numerical suffix starting from 1, and a corresponding "description" key with a value that is a concise, up to six-word sentence describing each main, distinct object or person in the image. Each pair should uniquely describe one element without repeating keys. An example: {"object1": { "description": "Man in red hat walking." },"object2": { "description": "Wooden pallet with boxes." },"object3": { "description": "Cardboard boxes stacked." },"object4": { "description": "Man in green vest standing." }}'}
                ]
                }
        ]
        try:
            response = client.chat.completions.create(
                model="qwen-vl-plus",
                messages=messages
            )
            print(response.choices[0].message.content)
            if return_json:
                return list(set(self.extract_descriptions_from_incomplete_json(response.choices[0].message["content"])))
            return response.choices[0].message["content"]
        except Exception as e:
            raise ValueError(f"Error during inference: {e}")

    def extract_descriptions_from_incomplete_json(self, json_like_str):
        last_object_idx = json_like_str.rfind(',"object')
        if last_object_idx != -1:
            json_str = json_like_str[:last_object_idx] + '}'
        else:
            json_str = json_like_str.strip()
            if not json_str.endswith('}'):
                json_str += '}'

        try:
            json_obj = json.loads(json_str)
            descriptions = [details['description'].replace(".", "") for key, details in json_obj.items() if 'description' in details]
            return descriptions
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing JSON: {e}")

