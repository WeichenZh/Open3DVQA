#!/bin/bash

# Define the main folder path argument
# MAIN_FOLDER_PATH="/path/to/main/folder"
# OUTPUT_FILE="/path/to/OUTPUT_FILE"
# SAVE_ROOT="/path/to/SAVE_ROOT"
MAIN_FOLDER_PATH="../data/open3dvqa"
OUTPUT_FILE="../data/open3dvqa/merged.json"
SAVE_ROOT="../data/open3dvqa"

# Run the Python scripts in sequence

python gpt4_caption.py --main-folder-path $MAIN_FOLDER_PATH

python prompts_processor.py --main-folder-path $MAIN_FOLDER_PATH

python merge_json.py --root-folder $MAIN_FOLDER_PATH  --output-file $OUTPUT_FILE 

python filter_and_split_data.py --root-folder $MAIN_FOLDER_PATH --save-root $SAVE_ROOT
