# Open3DVQA: A Benchmark for Comprehensive Spatial Reasoning with Multimodal Large Language Model in Open Space


[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](CODE_LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-mit-green.svg)](DATA_LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)


______________________________________________________________________

## 💡 Introduction

[**Open3DVQA: A Benchmark for Comprehensive Spatial Reasoning with Multimodal Large Language Model in Open Space**](<https://www.arxiv.org/abs/2503.11094>)

Open3DVQA is a benchamrk to comprehensively evaluate the spatial reasoning capacities of current SOTA foundation models in open 3D space. It consists of 9k VOA samples, collected using aneffcient semi-automated tool in a high-fdelity urban simulator. 

______________________________________________________________________

## 📢 News
- **Mar-15-2025**- Open3DVQA preprint released at [Arxiv](https://www.arxiv.org/abs/2503.11094)!
- **Feb-27-2025**- Open3DVQA code/dataset released! 🔥
______________________________________________________________________

## Open3DVQA Dataset

Please download the Open3DVQA Dataset from [google drive](https://drive.google.com/drive/folders/1CKSavijr67U8jKMg_kpYNKKs9Nk_bmg1?usp=sharing). If you want to prepare for your own dataset, please see the following dataset synthesis pipeline.

______________________________________________________________________

## Dataset Synthesis Pipeline

We've also made the dataset synthesis pipeline available. You can find the code and instructions in the [processor](processor) folder.

Please clone this repository and change path to the floder. Then use the following command to get the open3dvqa dataset.
```bash
   cd Open3DVQA
```
Place your own boundingbox.json path extracted from Airsim and change your boundingbox.json path in the id_processor.py. The structure should be as follow:
```
Open3DVQA/
├── utils/
├── processor/
│   ├── id_processor.py
│   ├── caption_processor.py
│   ├── ...
├── data/
│   ├── open3dvqa/
│   │   ├── 1/
│   │   │   ├── depth/
│   │   │   ├── state/
│   │   │   ├── rgb/
│   │   │   ├── visible_objs/
│   │   ├── ...
│   ├── object_info.json
│   ├── Buildingbbox.json
│   ├── ...
```
Run id_processor.py to get ids of interested objects. After that, run caption_processor.py to get the boundingbox and egocentric coordinates. Fill your own gpt api key in the gpt4_caption.py and run the create_vqa.sh to get your own dataset.

```bash
   python processor/id_processor.py
   python processor/caption_processor.py
   bash processor/create_vqa.sh
```

Feel free to report any issues or unexpected results you encounter.


______________________________________________________________________

## 🙏 Acknowledgement

We have used code snippets from different repositories, especially from: LLaVA, Qwen2-VL and VQASynth. We would like to acknowledge and thank the authors of these repositories for their excellent work.
