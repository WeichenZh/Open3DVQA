import json
from openai import OpenAI
from tqdm import tqdm
from datetime import datetime
import os


result_path = "response_result/gpt-4o_responses.json"
filename = os.path.basename(result_path)
model_name = filename.split("_")[0]
log_file = f"evaluation_log/{model_name}.txt"

def log_progress(index, correct, total):
    accuracy = correct / total if total > 0 else 0.0
    with open(log_file, 'a', encoding='utf-8') as logf:
        logf.write(f"[{datetime.now()}] Step {index}: Accuracy = {accuracy:.4f} ({correct}/{total})\n")

def check_match(question, answer, response):

    prompt = f"""
You should help me to evaluate the response given the question and the correct answer.
To mark a response, you should output a single integer between 0 and 1.
1 means that the response perfectly matches the answer.
0 means that the response is completely different from the answer.
"""

    post_fix = f"""
Your Turn:
Question: {question}
Answer: {answer}
Response: {response}
    """

    # content = prompt + examples.format(question=question) + post_fix.format(question, answer, response)
    content = prompt + post_fix
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://api.openai.com/v1"  # default OpenAI API endpoint
    )
    
    response = client.chat.completions.create(
        timeout=75,
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to evaluate qa quality."},
            {"role": "user", "content": content},
        ],
    )
    return response.choices[0].message.content

def evaluate(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_items = []
    # flatten the nested structure
    for dataset_name, scenes in data.items():  
        for scene_name, items in scenes.items():
            for item in items: 
                all_items.append((dataset_name, scene_name, item))

    total = 0
    correct = 0

    for i, (dataset, scene, item) in enumerate(tqdm(all_items, desc="Evaluating"), 1):
        # if i <= 10230:
        #     continue
        question = item.get("question", "")
        pred = item.get("response", "")
        gt = item.get("answer", "")
        if pred and gt:
            score = check_match(question, pred, gt)
            while score not in ["0", "1"]:
                print(f"Invalid score: {score}. Retrying...")
                score = check_match(question, pred, gt)
            if score == "1":
                correct += 1
                total += 1
            elif score == "0":
                correct += 0
                total += 1
            log_progress(i, correct, total)

    accuracy = correct / total if total > 0 else 0.0
    print(f"\n Accuracy: {accuracy:.4f} ({correct}/{total})")
    log_progress("Final", correct, total)

if __name__ == "__main__":
    evaluate(result_path)
