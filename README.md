# Open3DVQA: A Benchmark for Embodied Spatial Concept Reasoning with Multimodal Large Language Model in Open Space

Open3DVQA is a benchamrk to comprehensively evaluate the spatial reasoning capacities of current SOTA foundation models in open 3D space. It consists of 89k VQA samples, collected using aneffcient semi-automated tool in a high-fdelity urban simulator.

## Open3DVQA Benchmark

We present Open3DVQA, a novel benchmark for evaluating MLLMs' ability to reason about complex spatial relationships from an aerial perspective. The benchmark comprises **89k** QA pairs spanning **7** general spatial reasoning tasks—multiple-choice, true/false, and short-answer formats—and supports both visual and point cloud modalities. The questions are automatically generated from spatial relations extracted from both real-world and simulated aerial scenes.

**Note 1:** We propose **Open3DVQA**, a novel question-answering benchmark designed for spatial reasoning in 3D urban environments. The benchmark encompasses four distinct spatial perspectives and **7** task types, providing a comprehensive evaluation of an embodied agent’s 3D spatial reasoning capabilities.

**Note 2:** We introduce a scalable **QA generation pipeline** that extracts 3D spatial relationships and generates diverse QA formats from a single RGB image. We design a plug-and-play multi-modal correction flow that leverages available ground-truth information across modalities to reduce error accumulation and ensure high-quality QAs.

**Note 3:** We evaluate mainstream MLLMs on Open3DVQA, revealing their current limitations in spatial reasoning and analyzing their sim-to-real capacities.

### Multiple Modalities


| Sample             | RGB                                                       | Depth                     |Caption & Bounding Box                                                     | Mask                                                      | PointCloud                                                |
|:------------:|:---------------------------------------------------------:|:---------------------------------------------------------:|:---------------------------------------------------------:|:---------------------------------------------------------:|:----------------------------------------------------------:|
| **1** | <img src="figure/rgb_1.png" height="65px"/>                | <img src="figure/depth_1.png" height="65px"/>              | <img src="figure/cap_1.png" height="65px"/>              | <img src="figure/mask_1.png" height="65px"/>              | <img src="figure/pcd_1.png" height="65px"/>                |
| **2** | <img src="figure/rgb_2.png" height="65px"/>                | <img src="figure/depth_2.png" height="65px"/>              | <img src="figure/cap_2.png" height="65px"/>              | <img src="figure/mask_2.png" height="65px"/>              | <img src="figure/pcd_2.png" height="65px"/>                |
| **3** | <img src="figure/rgb_3.png" height="65px"/>                | <img src="figure/depth_3.png" height="65px"/>              | <img src="figure/cap_3.png" height="65px"/>              | <img src="figure/mask_3.png" height="65px"/>              | <img src="figure/pcd_3.png" height="65px"/>                |
| **4** | <img src="figure/rgb_4.png" height="65px"/>                | <img src="figure/depth_4.png" height="65px"/>              | <img src="figure/cap_4.png" height="65px"/>              | <img src="figure/mask_4.png" height="65px"/>              | <img src="figure/pcd_4.png" height="65px"/>                |
| **5** | <img src="figure/rgb_5.png" height="65px"/>                | <img src="figure/depth_5.png" height="65px"/>              | <img src="figure/cap_5.png" height="65px"/>              | <img src="figure/mask_5.png" height="65px"/>              | <img src="figure/pcd_5.png" height="65px"/>                |
| **6** | <img src="figure/rgb_6.png" height="65px"/>                | <img src="figure/depth_6.png" height="65px"/>              | <img src="figure/cap_6.png" height="65px"/>              | <img src="figure/mask_6.png" height="65px"/>              | <img src="figure/pcd_6.png" height="65px"/>                |



### QA Templates

<table>
  <tr>
    <th style="text-align: center; vertical-align: middle;">QA Tasks</th>
    <th style="text-align: center; vertical-align: middle;">Intention</th>
    <th style="text-align: center; vertical-align: middle;">Examples</th>
  </tr>
  <tr>
    <td style="text-align: center; vertical-align: middle;"><strong>Allocentric Size Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      To infer relative size relationships <strong>between two objects in space</strong>, such as longer/shorter, wider/narrower, taller/shorter, larger/smaller.
    </td>
    <td>
      <table>
        <tr>
          <td>
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td>
            <strong>Question:</strong> Between the white building with blue stripes and the tall beige apartment building nearby, which one has more width?<br>
            <strong>Answer:</strong> Appearing wider between the two is white building with blue stripes.<br>
          </td>
          <td style="width: 100px;"><img src="figure/rgb_2.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;"><strong>Allocentric Distance Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      To infer straight-line, vertical or horizontal <strong>distances between objects</strong>.
    </td>
    <td>
      <table>
        <tr>
          <td>
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td>
            <strong>Question:</strong> Between the white building with blue stripes and the tall beige apartment building nearby, which one has more width?<br>
            <strong>Answer:</strong> Appearing wider between the two is white building with blue stripes.<br>
          </td>
          <td style="width: 100px;"><img src="figure/rgb_2.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;"><strong>Egocentric Direction Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      To infer the direction of an object <strong>relative to the agent</strong>, such as left, right, up and down.
    </td>
    <td>
      <table>
        <tr>
          <td>
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td>
            <strong>Question:</strong> Between the white building with blue stripes and the tall beige apartment building nearby, which one has more width?<br>
            <strong>Answer:</strong> Appearing wider between the two is white building with blue stripes.<br>
          </td>
          <td style="width: 100px;"><img src="figure/rgb_2.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;"><strong>Egocentric Distance Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      To infer the straight-line distance of an object <strong>from the agent</strong>.
    </td>
    <td>
      <table>
        <tr>
          <td>
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td>
            <strong>Question:</strong> Between the white building with blue stripes and the tall beige apartment building nearby, which one has more width?<br>
            <strong>Answer:</strong> Appearing wider between the two is white building with blue stripes.<br>
          </td>
          <td style="width: 100px;"><img src="figure/rgb_2.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;"><strong>Allocentric-Egocentric Transformation Direction Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      The agent <strong>infers the direction of objects</strong> relative to itself based on its movement.
    </td>
    <td>
      <table>
        <tr>
          <td>
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td>
            <strong>Question:</strong> Between the white building with blue stripes and the tall beige apartment building nearby, which one has more width?<br>
            <strong>Answer:</strong> Appearing wider between the two is white building with blue stripes.<br>
          </td>
          <td style="width: 100px;"><img src="figure/rgb_2.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;"><strong>Allocentric-Egocentric Transformation Distance Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      The agent <strong>infers object distance</strong> in the horizontal or vertical direction relative to itself.
    </td>
    <td>
      <table>
        <tr>
          <td>
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td>
            <strong>Question:</strong> Between the white building with blue stripes and the tall beige apartment building nearby, which one has more width?<br>
            <strong>Answer:</strong> Appearing wider between the two is white building with blue stripes.<br>
          </td>
          <td style="width: 100px;"><img src="figure/rgb_2.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td style="text-align: center; vertical-align: middle;"><strong>Object-Centric Size Reasoning</strong></td>
    <td style="text-align: center; vertical-align: middle;">
      To infer the <strong>absolute size</strong> of a single object, such as its length, width or height.
    </td>
    <td>
      <table>
        <tr>
          <td>
            <strong>Question:</strong> Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?<br>
            <strong>Answer:</strong> Yes, the red storefront with chinese text is shorter than the white building with blue stripes.
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
        </tr>
        <tr>
          <td>
            <strong>Question:</strong> Between the white building with blue stripes and the tall beige apartment building nearby, which one has more width?<br>
            <strong>Answer:</strong> Appearing wider between the two is white building with blue stripes.<br>
          </td>
          <td style="width: 100px;"><img src="figure/rgb_2.png" height="80px"/></td>
        </tr>
      </table>
    </td>
  </tr>
</table>

### Response Examples

<table>
  <tr>
    <th style="text-align: center; vertical-align: middle;">QA Tasks</th>
    <th style="text-align: center; vertical-align: middle;">Questions</th>
    <th style="text-align: center; vertical-align: middle;">Responses</th>
  </tr>
  <tr>
    <td style="text-align: center; vertical-align: middle;"><strong>Allocentric Size Reasoning</strong></td>
    <td>
      <table>
        <tr>
          <td style="text-align: center; vertical-align: middle;">
            Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
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
    <td style="text-align: center; vertical-align: middle;"><strong>Allocentric Distance Reasoning</strong></td>
    <td>
      <table>
        <tr>
          <td>
            Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
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
    <td style="text-align: center; vertical-align: middle;"><strong>Egocentric Direction Reasoning</strong></td>
    <td>
      <table>
        <tr>
          <td>
            Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
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
    <td style="text-align: center; vertical-align: middle;"><strong>Egocentric Distance Reasoning</strong></td>
    <td>
      <table>
        <tr>
          <td>
            Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
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
    <td style="text-align: center; vertical-align: middle;"><strong>Allocentric-Egocentric Transformation Direction Reasoning</strong></td>
    <td>
      <table>
        <tr>
          <td>
            Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
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
    <td style="text-align: center; vertical-align: middle;"><strong>Allocentric-Egocentric Transformation Distance Reasoning</strong></td>
    <td>
      <table>
        <tr>
          <td>
            Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
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
    <td style="text-align: center; vertical-align: middle;"><strong>Object-Centric Size Reasoning</strong></td>
    <td>
      <table>
        <tr>
          <td>
            Does the red storefront with chinese text have a lesser height compared to the white building with blue stripes?
          </td>
          <td style="width: 100px;"><img src="figure/rgb_1.png" height="80px"/></td>
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

## Data Curation

AirScape takes the current observations and motion intentions as input and outputs future embodied sequence observations (videos). 
Below are examples of videos generated on the test set.

### Simulator

| Example |                                          Prediction                                           |                                                                                                                             Motion Intention                                                                                                                              |
|:-------:|:---------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| **1** |         <img src="figure/generated_example/00819_urbanvideo_test.gif" width="100%"/>          |                                                      The drone moved forward with its camera pointed straight ahead, capturing a stationary view of high-rise buildings, a landscaped garden, and a pond.                                                       |
| **2** |         <img src="figure/generated_example/00840_urbanvideo_test.gif" width="100%"/>          |                             The drone rotated counterclockwise inplace, with its camera gimbal angled downward, and concluded its flight above a courtyard featuring a circular fountain, swimming pools, and surrounding greenery.                             |
| **3** |         <img src="figure/generated_example/00846_urbanvideo_test.gif" width="100%"/>          |                                                             The drone hovered in place while gradually rotating to the left, ended up facing a broader view of the buildings and the street below.                                                              |
| **4** |         <img src="figure/generated_example/00930_urbanvideo_test.gif" width="100%"/>          |                                  The drone tilts up its camera, moves slightly forward while maintaining a steady view of a fountain plaza and surrounding area, then holds position for an overhead perspective of the scene.                                  |
| **5** |      <img src="figure/generated_example/01035_NAT2021_test_N02029_4.gif" width="100%"/>       |                                          No obvious tracking of a target, the drone moving forward along a road while maintaining the gimbal angle, with its final position being farther down the illuminated street.                                          |
| **6** |      <img src="figure/generated_example/01247_NAT2021_test_N04039_2.gif" width="100%"/>       |                    A group of pedestrians moving from left to right along a walkway, while the drone rotates rightward slowly and its camera gimbal adjusts slightly to follow their motion, keeping them centered and visible in the frame.                    |
| **7** |      <img src="figure/generated_example/01374_NAT2021_test_N08024_3.gif" width="100%"/>       | The drone ascends while capturing a night-time view of a road with vehicles moving forward (away from the drone) and brightly lit buildings in the distance, without obvious tracking or significant camera gimbal movements. |
| **8** |    <img src="figure/generated_example/11954_WebUAV3M_val_apartment_3_1.gif" width="100%"/>    |                                                                  The drone flies forward, keeping the skyline of the city centered in its field of view.                                                                   |
| **9** | <img src="figure/generated_example/11992_WebUAV3M_val_container_ship_6_0.gif" width="100%"/>  |                                            The drone tracks a cargo ship moving forward along the river, while flying to the right and rotate to the left, maintaining the ship in the center of the field of view.                                             |
| **10** |  <img src="figure/generated_example/11964_WebUAV3M_val_bulk_carrier_32_0.gif" width="100%"/>  |                                                                               The drone flies to the right, maintaining the current altitude and keeping the gimbal angle level.                                                                                |
| **11** |    <img src="figure/generated_example/11977_WebUAV3M_val_climbing_2_2.gif" width="100%"/>     |                         The drone flies to the left while rotating to the right, rotating clockwise about 45 degrees around the pagoda in the field of view, while keeping the pagoda and surrounding structures centered in the frame.                         |
| **12** | <img src="figure/generated_example/11980_WebUAV3M_val_climbing_stairs_5_1.gif" width="100%"/> |                                       The drone flies to the left while rotating to the right, rotating clockwise slowly around the pagoda in the field of view, while keeping the statue centered in its field of view.                                        |
| **13** |   <img src="figure/generated_example/12026_WebUAV3M_val_harvester_23_1.gif" width="100%"/>    |                              The drone is moving forward, adjusting the pan tilt angle downwards to track the movement of two agricultural vehicles proceeding forward in tandem, maintaining them centered in its field of view.                               |
| **14** |   <img src="figure/generated_example/12033_WebUAV3M_val_harvester_34_6.gif" width="100%"/>    |                                      The drone follows a combine harvester moving forward through a field, keeping the harvester in the center of its field of view while maintaining a steady altitude and camera angle.                                       |

### Realworld

## QA Generation Pipeline

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

## Inference & Evaluation

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

## Acknowledgement

We have used code snippets from different repositories, especially from: LLaVA, Qwen2-VL and VQASynth. We would like to acknowledge and thank the authors of these repositories for their excellent work.
