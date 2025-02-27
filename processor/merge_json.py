import os
import json
import argparse

def merge_json_files(args):
    # Used to store the merged data
    root_folder = args.root_folder
    output_file = args.output_file
    merged_data = []

    # Get the direct subfolders under root_folder
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        # Ensure it is a folder
        if os.path.isdir(folder_path):
            # Traverse the files in the subfolder
            for filename in os.listdir(folder_path):
                if filename.endswith('.json'):
                    file_path = os.path.join(folder_path, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            if data == []:
                                continue
                            else:
                                merged_data.append(data)
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

    # Write the merged data to the output JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)

def main(args):
    root_folder = args.root_folder
    output_file = args.output_file
    merge_json_files(root_folder, output_file)
    print(f"Merged file has been saved to {output_file}")

    total_elements = 0
    with open(output_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # If it is a list, count the length of the list
        if isinstance(data, list):
            total_elements += len(data)
        # If it is a dictionary, count the number of key-value pairs in the dictionary
        elif isinstance(data, dict):
            total_elements += len(data)
        else:
            print(f"Unsupported JSON data format: {output_file}")
    print(total_elements)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-folder", type=str, required=True, help="path to root directory")
    parser.add_argument("--output-file", type=str, required=True, help="path to output JSON file")
    args = parser.parse_args()
    main(args)