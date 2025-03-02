import numpy as np


def bbox_diagonal2vertice(p1, p2):
    min_point = np.minimum(p1, p2)
    max_point = np.maximum(p1, p2)
    # print(min_point, max_point)

    bbox = np.array([
        [min_point[0], min_point[1], min_point[2]],  # P1
        [max_point[0], min_point[1], min_point[2]],  # P2
        [min_point[0], max_point[1], min_point[2]],  # P3
        [max_point[0], max_point[1], min_point[2]],  # P4
        [min_point[0], min_point[1], max_point[2]],  # P5
        [max_point[0], min_point[1], max_point[2]],  # P6
        [min_point[0], max_point[1], max_point[2]],  # P7
        [max_point[0], max_point[1], max_point[2]]  # P8
    ])
    return bbox


def calc_iou(box1, box2):
    # box1 和 box2 格式为 (x1, y1, x2, y2)
    x1_inter = max(box1[0], box2[0])
    y1_inter = max(box1[1], box2[1])
    x2_inter = min(box1[2], box2[2])
    y2_inter = min(box1[3], box2[3])

    inter_width = max(0, x2_inter - x1_inter)
    inter_height = max(0, y2_inter - y1_inter)
    intersection_area = inter_width * inter_height

    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])

    union_area = box1_area + box2_area - intersection_area

    iou = intersection_area / union_area if union_area > 0 else 0
    return iou

def calc_vis_iou(box1, box2):
    # iou的公式为 intersection / area_of_box2
    # 这种做法是为了判断box1是否完全遮挡了box2
    x1_inter = max(box1[0], box2[0])
    y1_inter = max(box1[1], box2[1])
    x2_inter = min(box1[2], box2[2])
    y2_inter = min(box1[3], box2[3])

    inter_width = max(0, x2_inter - x1_inter)
    inter_height = max(0, y2_inter - y1_inter)
    intersection_area = inter_width * inter_height

    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])

    union_area = box2_area

    iou = intersection_area / union_area if union_area > 0 else 0
    return iou
