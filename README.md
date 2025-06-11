# Open3DVQA: A Benchmark for Embodied Spatial Concept Reasoning with Multimodal Large Language Model in Open Space

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](CODE_LICENSE)
[![Code License](https://img.shields.io/badge/Data%20License-Apache_2.0-green.svg)](CODE_LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)

______________________________________________________________________

[**📄 Open3DVQA: A Benchmark for Comprehensive Spatial Reasoning with Multimodal Large Language Model in Open Space**](<https://www.arxiv.org/abs/2503.11094>)

We present Open3DVQA, a novel benchmark for evaluating MLLMs' ability to reason about complex spatial relationships from an aerial perspective.The QAs are automatically generated from spatial relations extracted from both real-world and simulated aerial scenes.

![Open3DVQA Overview](figure/data_overview.jpg)

______________________________________________________________________

## 📢 News
- **June-03-2025**- Open3DVQA v2 is released at [Open3DVQA-v2](https://github.com/WeichenZh/Open3DVQA/tree/o3dvqa_v2)! 🔥
- **Mar-15-2025**- Open3DVQA preprint released at [Arxiv](https://www.arxiv.org/abs/2503.11094)! 🔥
- **Feb-27-2025**- Open3DVQA code/dataset released! 🔥
______________________________________________________________________

## ✅ Open3DVQA Benchmark

Open3DVQA is a novel benchmark evaluating MLLMs' ability to reason about complex spatial relationships from an aerial view. It contains **89k** QA pairs across **7** spatial reasoning tasks—including multiple-choice, true/false, and short-answer formats—and supports both visual and point cloud data. Questions are automatically generated from spatial relations in real-world and simulated aerial scenes.

**💡 Key highlights:**

- Covers four spatial perspectives and **7** task types for comprehensive open 3D spatial reasoning evaluation.
- Introduces a scalable **QA generation pipeline** that extracts 3D spatial relationships and creates diverse QA formats from a single RGB image, with a multi-modal correction flow to ensure quality.
- Benchmarks mainstream MLLMs, revealing their current spatial reasoning limitations and sim-to-real generalization capabilities.

### 📋 QA Templates

<table>
  <tr>
    <th style="text-align: center; vertical-align: middle;">QA Tasks</th>
    <th style="text-align: center; vertical-align: middle;">Intention</th>
    <th style="text-align: center; vertical-align: middle;">Examples</th>
  </tr>
  <tr>
    <td align="center"><strong>Allocentric Size Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      To infer relative size relationships <strong>between two objects in space</strong>, such as longer/shorter, wider/narrower, taller/shorter, larger/smaller.
    </td>
    <td>
      <table>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Is the modern building with vertical glass panels thinner than the curved white railing structure?<br>
            <strong>Answer:</strong> No, the modern building with vertical glass panels is not thinner than the curved white railing structure.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_4.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Which of these two, the white modular buildings with windows or the tall beige residential apartments, appears wider?<br>
            <strong>Answer:</strong> Appearing wider between the two is white modular buildings with windows.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_5.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Allocentric Distance Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      To infer straight-line, vertical or horizontal <strong>distances between objects</strong>.
    </td>
    <td>
      <table>
        <tr>
          <td width="360px">
            <strong>Question:</strong> How close is the white building with small square windows from the grey pathway leading to the building?<br>
            <strong>Answer:</strong> A distance of 32.15 meters exists between the white building with small square windows and the grey pathway leading to the building.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_3.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> How far is the row of parked white vans from the white building with blue stripes horizontally?<br>
            <strong>Answer:</strong> The row of parked white vans is 6.26 meters away from the white building with blue stripes horizontally.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Egocentric Direction Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      To infer the direction of an object <strong>relative to the agent</strong>, such as left, right, up and down.
    </td>
    <td>
      <table>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Is the white modular buildings with windows to the left of you from the viewer's perspective?<br>
            <strong>Answer:</strong> Yes, the white modular buildings with windows is to the left.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_5.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Which is closer to viewer, the white suv parked in foreground or the blue building with tree beside?<br>A:white suv parked in foreground B:blue building with tree beside C:Same D:Unknown<br>
            <strong>Answer:</strong> A.white suv parked in foreground.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_6.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Egocentric Distance Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      To infer the straight-line distance of an object <strong>from the agent</strong>.
    </td>
    <td>
      <table>
        <tr>
          <td width="360px">
            <strong>Question:</strong> How far is the red storefront with chinese text from you?<br>
            <strong>Answer:</strong> 29.0 meters
          </td>
          <td style="width: 90px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> How close is the white building with blue stripes from you?<br>
            <strong>Answer:</strong> The distance of the white building with blue stripes is 41.73 meters.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_2.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Allocentric-Egocentric Transformation Direction Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      The agent <strong>infers the direction of objects</strong> relative to itself based on its movement.
    </td>
    <td>
      <table>
        <tr>
          <td width="360px">
            <strong>Question:</strong> If you are at white building with small square windows, where will you find grey pathway leading to the building?<br>
            <strong>Answer:</strong> Grey pathway leading to the building is roughly at 9 o'clock from white building with small square windows.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_3.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> If you are at row of parked white vans, where will you find white building with blue stripes?<br>
            <strong>Answer:</strong> Row of parked white vans will find white building with blue stripes around the 10 o'clock direction.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Allocentric-Egocentric Transformation Distance Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      The agent <strong>infers object distance</strong> in the horizontal or vertical direction relative to itself.
    </td>
    <td>
      <table>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Could you provide the vertical distance between the white building with blue stripes and you?<br>
            <strong>Answer:</strong> 4.19 meters
          </td>
          <td style="width: 90px;"><img src="figure/rgb_2.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> How distant is the green foliage surrounding the structure from you horizontally?<br>
            <strong>Answer:</strong> Horizontally, 96.91 meters apart.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_3.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Object-Centric Size Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      To infer the <strong>absolute size</strong> of a single object, such as its length, width or height.
    </td>
    <td>
      <table>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Determine the horizontal dimensions of the dark stone lion sculpture with textured surface.<br>
            <strong>Answer:</strong> The dark stone lion sculpture with textured surface is 2.49 meters wide.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_7.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> How tall is the curved black streetlamp with modern design?<br>
            <strong>Answer:</strong> The height of the curved black streetlamp with modern design is 7.26 meters.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_8.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>
</table>

### 💬 Response Examples

<table>
  <tr>
    <th style="text-align: center; vertical-align: middle;">QA Tasks</th>
    <th style="text-align: center; vertical-align: middle;">Questions</th>
    <th style="text-align: center; vertical-align: middle;">Responses</th>
  </tr>
  <tr>
    <td align="center"><strong>Allocentric Size<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_4.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td width="300px">
            Is the modern building with vertical glass panels thinner than the curved white railing structure?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> No.✔️<br>
      <strong>Qwen2-VL-Finetuned:</strong> Incorrect, the modern building with vertical glass panels's width is not less than the curved white railing structure's.✔️<br>
      <strong>3D-LLM:</strong> The modern building with vertical glass panels is thinner than the curved white railing structure.❌
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Allocentric Distance<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_9.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td width="300px">
            How much distance is there between the wooden pavilion with blue metal pyramid roof and the gray stucco wall with minimalist design and structure?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> Based only on the provided image, it is not possible to determine an exact numerical distance between the wooden pavilion with the blue metal pyramid roof and the gray stucco wall with the minimalist design and structure. The image does not contain the necessary depth or scale information to calculate this measurement.❌<br>
      <strong>Qwen2-VL-Finetuned:</strong> 11.22 meters.❌<br>
      <strong>3D-LLM:</strong> The wooden pavilion with blue metal pyramid roof is a few meters away from the gray stucco wall with minimalist design and structure.❌
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Egocentric Direction<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_5.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td width="300px">
            Is the white modular buildings with windows to the left of you from the viewer's perspective?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> Yes, the white modular buildings with windows are to the left of you from the viewer's perspective (around 9 o'clock to 11 o'clock).✔️<br>
      <strong>Qwen2-VL-Finetuned:</strong> Correct, you'll find the white modular buildings with windows to the left.✔️<br>
      <strong>3D-LLM:</strong> The white modular buildings with windows are to the left of the viewer's perspective.✔️
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Egocentric Distance<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_9.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td width="300px">
            Can you give me an estimation of the distance between the wooden pavilion with blue metal pyramid roof and you?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> Based on the image, the distance between the wooden pavilion with blue metal pyramid roof and you is 10 meters.✔️<br>
      <strong>Qwen2-VL-Finetuned:</strong> The wooden pavilion with blue metal pyramid roof is 11.51 meters away.✔️<br>
      <strong>3D-LLM:</strong> The wooden pavilion with blue metal pyramid roof is approximately 3.05 meters tall.❌
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Allocentric-Egocentric<br>Transformation Direction<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_10.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td width="300px">
            If you are at white building with irregular windows, where will you find area with dense green foliage?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> If you are at the white building with irregular windows, you will find the area with dense green foliage at 12 o'clock.❌<br>
      <strong>Qwen2-VL-Finetuned:</strong> White building with irregular windows will find area with dense green foliage around the 7 o'clock direction.✔️<br>
      <strong>3D-LLM:</strong> The area with dense green foliage is near the white building with irregular windows.❌
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Allocentric-Egocentric<br>Transformation Distance<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_11.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td width="300px">
            Give me the vertical distance from the small wooden structure on ground to you.
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> -1.❌<br>
      <strong>Qwen2-VL-Finetuned:</strong> The vertical distance of the small wooden structure on ground is 21.52 meters.❌<br>
      <strong>3D-LLM:</strong> 0.❌
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Object-Centric<br>Size Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_7.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td width="300px">
            Determine the horizontal dimensions of the dark stone lion sculpture with textured surface.
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> I cannot determine the exact horizontal dimensions from the image alone.❌<br>
      <strong>Qwen2-VL-Finetuned:</strong> The dark stone lion sculpture with textured surface is 2.42 meters in width.✔️<br>
      <strong>3D-LLM:</strong> The horizontal dimensions of the dark stone lion sculpture with textured surface are.❌
    </td>
  </tr>
</table>

### 🖼️ Multiple Modalities

| Sample             | RGB                                                       | Depth                     |Caption & Bounding Box                                                     | Mask                                                      | PointCloud                                                |
|:------------:|:---------------------------------------------------------:|:---------------------------------------------------------:|:---------------------------------------------------------:|:---------------------------------------------------------:|:----------------------------------------------------------:|
| **1** | <img src="figure/rgb_1.png" height="55px"/>                | <img src="figure/depth_1.png" height="55px"/>              | <img src="figure/cap_1.png" height="55px"/>              | <img src="figure/mask_1.png" height="55px"/>              | <img src="figure/pcd_1.png" height="55px"/>                |
| **2** | <img src="figure/rgb_2.png" height="55px"/>                | <img src="figure/depth_2.png" height="55px"/>              | <img src="figure/cap_2.png" height="55px"/>              | <img src="figure/mask_2.png" height="55px"/>              | <img src="figure/pcd_2.png" height="55px"/>                |
| **3** | <img src="figure/rgb_3.png" height="55px"/>                | <img src="figure/depth_3.png" height="55px"/>              | <img src="figure/cap_3.png" height="55px"/>              | <img src="figure/mask_3.png" height="55px"/>              | <img src="figure/pcd_3.png" height="55px"/>                |
| **4** | <img src="figure/rgb_4.png" height="55px"/>                | <img src="figure/depth_4.png" height="55px"/>              | <img src="figure/cap_4.png" height="55px"/>              | <img src="figure/mask_4.png" height="55px"/>              | <img src="figure/pcd_4.png" height="55px"/>                |
| **5** | <img src="figure/rgb_5.png" height="55px"/>                | <img src="figure/depth_5.png" height="55px"/>              | <img src="figure/cap_5.png" height="55px"/>              | <img src="figure/mask_5.png" height="55px"/>              | <img src="figure/pcd_5.png" height="55px"/>                |
| **6** | <img src="figure/rgb_6.png" height="55px"/>                | <img src="figure/depth_6.png" height="55px"/>              | <img src="figure/cap_6.png" height="55px"/>              | <img src="figure/mask_6.png" height="55px"/>              | <img src="figure/pcd_6.png" height="55px"/>                |

______________________________________________________________________

## 🛠️ QA Generation Pipeline

![QA Generation Pipeline](figure/qa_pipeline.jpg)

We've also made the QA generation pipeline available. Before running the code, make sure you complete the following three steps:

**1. Set up the environment**

Install all required Python packages and dependencies. You can use the provided `requirements.txt`:

```bash
git clone https://github.com/WeichenZh/Open3DVQA.git
cd Open3DVQA
conda create -n o3dvqa python=3.10 -y
conda activate o3dvqa
pip install -r requirements.txt
```

**2. Prepare the GPT-4o API access**

You need access to the GPT-4o model via OpenAI’s API. Make sure your API key is correctly set as an environment variable:
```bash
export OPENAI_API_KEY=your_api_key_here
```

**3. Download dataset and models**
  
Please download the Open3DVQA dataset, ClipSeg and SAM: 

- [Open3DVQA dataset](https://huggingface.co/datasets/zzxslp/Open3DVQA)
- [ClipSeg model](https://huggingface.co/CIDAS/clipseg-rd64-refined)
- [SAM model](https://huggingface.co/facebook/sam-vit-h)

Organize all codes and resources according to the following directory structure:
```
Open3DVQA/
├── dataset/
│   ├── EmbodiedCity/
│   │   ├── Wuhan/
│   │   │   ├── depth/
│   │   │   ├── pose
│   │   │   ├── rgb/
│   │   │   ├── visible_objs/
│   │   │   ├── pointclouds/
│   │   │   ├── chunk_0.pkl
│   │   │   ├── ...
│   │   │   ├── merged_qa.json
│   ├── RealworldUAV/
│   │   ├── Lab/
│   │   ├── ...
│   ├── UrbanScene/
│   │   ├── Campus
│   │   ├── ...
│   ├── WildUAV/
│   │   ├── Wuhan/
├── vqasynth/
│   ├── models/
│   │   ├── clipseg/
│   │   ├── sam/
│   ├── ...
├── qa_pipeline.py
├── inference.py
├── evaluation.py
├── processor/
│   ├── process_caption.py
│   ├── process_depth.py
│   ├── process_segment.py
│   ├── ...
├── requirements.txt
```


Open `qa_pipeline.py` and set the `data_dir` variable to the scene you want to process. For example: `data_dir = dataset/RealworldUAV`

After saving your changes, run the script to start the QA generation process:

```bash
python qa_pipeline.py
```

The script will process the specified scene and generate QA pairs automatically. Input files are `rgb/`, `depth/` and `pose/`. Output files contain `pointclouds`, `chunk_*.pkl` and `merged_qa.json`.

______________________________________________________________________

## 🚀 Inference & Evaluation

We also provide scripts for model inference and evaluation:

- **`inference.py`**  
  This script allows you to perform QA using large language models (e.g., GPT-4o) via API. It takes prepared multimodal inputs and sends prompts to the model for response answer.

```bash
python inference.py
```

- **`evaluation.py`**  
  This script is used to evaluate the accuracy of the model-responsed answers. It compares the predicted answers against ground truth answers to compute evaluation metrics such as accuracy.

```bash
python evaluation.py
```

______________________________________________________________________

## 🙏 Acknowledgement

We have used code snippets from different repositories, especially from: LLaVA, Qwen2-VL and VQASynth. We would like to acknowledge and thank the authors of these repositories for their excellent work.
