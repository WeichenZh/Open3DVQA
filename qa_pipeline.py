import subprocess
import os
import time

data_dir = r"O3DVQA/EmbodiedCity/Wuhan"
seqs = os.listdir(data_dir)

for idx, seq in enumerate(seqs):
    seq_data_path = os.path.join(data_dir, seq)
    image_dir = os.path.join(seq_data_path, 'rgb')
    output_dir = seq_data_path

    commands = [
        f"python ./processor/process_caption.py --output_dir {output_dir} --image_dir {image_dir}",
        f"python ./processor/process_depth.py --output_dir {output_dir}",
        f"python ./processor/process_segment.py --output_dir {output_dir}",
        f"python ./processor/process_pointcloud.py --output_dir {output_dir}",
        f"python ./processor/process_prompts.py --output_dir {output_dir} --image_dir {image_dir}",
        f"python ./processor/generate_mask.py --output_dir {output_dir}"
    ]
    start_time = time.time()

    for command in commands:
        start_time_cmd = time.time()
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        if result.returncode != 0:
            print(f"Command failed: {command}")
            print(f"Error output:\n{result.stderr}")
            break
        end_time_cmd = time.time()
        print(f"Command finished: {command}. Time taken: {end_time_cmd - start_time_cmd:.2f} seconds")
    end_time = time.time()
    print(f"{idx} vqa finished. Saved images in {output_dir}. Time taken: {end_time - start_time:.2f} seconds")
