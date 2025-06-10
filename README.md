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
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Who is positioned more to the right, the white building with blue stripes or the tall beige apartment building nearby?<br>
            <strong>Answer:</strong> From the viewer's perspective, white building with blue stripes appears more on the right side.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_2.png" height="80px"/></td>
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
            <strong>Question:</strong> Is the position of the modern building with vertical glass panels more distant than that of the curved white railing structure?<br>
            <strong>Answer:</strong> Yes, it is.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_4.png" height="80px"/></td>
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
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
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
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
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
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_3.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_4.png" height="80px"/></td>
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
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_5.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_6.png" height="80px"/></td>
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
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td width="360px">
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 90px;"><img src="figure/rgb_2.png" height="80px"/></td>
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
            <img src="figure/rgb_1.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td align="left">
            Does the red storefront with Chinese<br>
            text have a lesser height compared<br>
            to the white building with blue stripes?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>Qwen2-VL-Finetuned:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>3D-LLM:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Allocentric Distance<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_2.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td align="left">
            Does the red storefront with Chinese<br>
            text have a lesser height compared<br>
            to the white building with blue stripes?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>Qwen2-VL-Finetuned:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>3D-LLM:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Egocentric Direction<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_3.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td align="left">
            Does the red storefront with Chinese<br>
            text have a lesser height compared<br>
            to the white building with blue stripes?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>Qwen2-VL-Finetuned:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>3D-LLM:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Egocentric Distance<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_4.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td align="left">
            Does the red storefront with Chinese<br>
            text have a lesser height compared<br>
            to the white building with blue stripes?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>Qwen2-VL-Finetuned:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>3D-LLM:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Allocentric-Egocentric<br>Transformation Direction<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_5.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td align="left">
            Does the red storefront with Chinese<br>
            text have a lesser height compared<br>
            to the white building with blue stripes?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>Qwen2-VL-Finetuned:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>3D-LLM:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Allocentric-Egocentric<br>Transformation Distance<br>Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_6.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td align="left">
            Does the red storefront with Chinese<br>
            text have a lesser height compared<br>
            to the white building with blue stripes?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>Qwen2-VL-Finetuned:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>3D-LLM:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
    </td>
  </tr>

  <tr>
    <td align="center"><strong>Object-Centric<br>Size Reasoning</strong></td>
   <td>
      <table>
        <tr>
          <td align="center">
            <img src="figure/rgb_1.png" height="100px" />
          </td>
        </tr>
        <tr>
          <td align="left">
            Does the red storefront with Chinese<br>
            text have a lesser height compared<br>
            to the white building with blue stripes?
          </td>
        </tr>
      </table>
   </td>
    <td>
      <strong>Gemini-2.5-Flash:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>Qwen2-VL-Finetuned:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.<br>
      <strong>3D-LLM:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
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

We've also made the dataset synthesis pipeline available. You can find the code and instructions in the [processor](processor) folder.

![QA Generation Pipeline](figure/qa_pipeline.jpg)

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

## 🚀 Inference & Evaluation

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
