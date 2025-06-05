import random
import numpy as np
import math
from itertools import combinations
from utils.prompt_templates import *


# Predicate prompts

def human_like_distance(distance_meters):
    if distance_meters > 1000:
        human_read_distance = round(distance_meters / 1000, 2)
        return f"{human_read_distance} kilometers"
    else:
        human_read_distance = round(distance_meters, 2)
        return f"{human_read_distance} meters"


def left_predicate(A, B):
    template_questions = left_predicate_questions
    true_responses = left_true_responses
    false_responses = left_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    is_left = A_pos[0] < B_pos[0]  # Compare X coordinates

    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_left else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def right_predicate(A, B):
    template_questions = right_predicate_questions
    true_responses = right_true_responses
    false_responses = right_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    is_right = A_pos[0] > B_pos[0]  # Compare X coordinates

    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_right else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def above_predicate(A, B):
    template_questions = above_predicate_questions
    true_responses = above_true_responses
    false_responses = above_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    is_above = A_pos[1] < B_pos[1]

    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_above else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def below_predicate(A, B):
    template_questions = below_predicate_questions
    true_responses = below_true_responses
    false_responses = below_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    is_below = A_pos[1] > B_pos[1]

    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_below else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def wide_predicate(A, B):
    template_questions = wide_predicate_questions
    true_responses = wide_true_responses
    false_responses = wide_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    X_A = {point[0] for point in A_bbox}
    X_B = {point[0] for point in B_bbox}

    width_A = abs(max(X_A) - min(X_A))
    width_B = abs(max(X_B) - min(X_B))

    is_wider = width_A > width_B

    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_wider else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def big_predicate(A, B):
    template_questions = big_predicate_questions
    true_responses = big_true_responses
    false_responses = big_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    X_A = {point[0] for point in A_bbox}
    Y_A = {point[1] for point in A_bbox}
    Z_A = {point[2] for point in A_bbox}

    X_B = {point[0] for point in B_bbox}
    Y_B = {point[1] for point in B_bbox}
    Z_B = {point[2] for point in B_bbox}

    # 计算宽度 (x方向差距), 深度 (y方向差距), 高度 (z方向差距)
    width_A = abs(max(X_A) - min(X_A))
    height_A = abs(max(Y_A) - min(Y_A))
    depth_A = abs(max(Z_A) - min(Z_A))
    volume_A = width_A * depth_A * height_A

    width_B = abs(max(X_B) - min(X_B))
    height_B = abs(max(Y_B) - min(Y_B))
    depth_B = abs(max(Z_B) - min(Z_B))
    volume_B = width_B * depth_B * height_B

    is_bigger = volume_A > volume_B

    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_bigger else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def tall_predicate(A, B):
    template_questions = tall_predicate_questions
    true_responses = tall_true_responses
    false_responses = tall_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    Y_A = {point[1] for point in A_bbox}
    Y_B = {point[1] for point in B_bbox}

    height_A = abs(max(Y_A) - min(Y_A))
    height_B = abs(max(Y_B) - min(Y_B))


    is_taller = height_A > height_B

    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_taller else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def short_predicate(A, B):
    template_questions = short_predicate_questions
    true_responses = short_true_responses
    false_responses = short_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    Y_A = {point[1] for point in A_bbox}
    Y_B = {point[1] for point in B_bbox}

    height_A = abs(max(Y_A) - min(Y_A))
    height_B = abs(max(Y_B) - min(Y_B))


    is_shorter = height_A < height_B

    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_shorter else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def thin_predicate(A, B):
    template_questions = thin_predicate_questions
    true_responses = thin_true_responses
    false_responses = thin_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    X_A = {point[0] for point in A_bbox}
    X_B = {point[0] for point in B_bbox}

    width_A = abs(max(X_A) - min(X_A))
    width_B = abs(max(X_B) - min(X_B))

    is_thinner = width_A < width_B

    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_thinner else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def small_predicate(A, B):
    template_questions = small_predicate_questions
    true_responses = small_true_responses
    false_responses = small_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    X_A = {point[0] for point in A_bbox}
    Y_A = {point[1] for point in A_bbox}
    Z_A = {point[2] for point in A_bbox}

    X_B = {point[0] for point in B_bbox}
    Y_B = {point[1] for point in B_bbox}
    Z_B = {point[2] for point in B_bbox}

    # 计算宽度 (x方向差距), 深度 (y方向差距), 高度 (z方向差距)
    width_A = abs(max(X_A) - min(X_A))
    height_A = abs(max(Y_A) - min(Y_A))
    depth_A = abs(max(Z_A) - min(Z_A))
    volume_A = width_A * depth_A * height_A

    width_B = abs(max(X_B) - min(X_B))
    height_B = abs(max(Y_B) - min(Y_B))
    depth_B = abs(max(Z_B) - min(Z_B))
    volume_B = width_B * depth_B * height_B

    is_smaller = volume_A < volume_B

    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_smaller else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def behind_predicate(A, B):
    template_questions = behind_predicate_questions
    true_responses = behind_true
    false_responses = behind_false

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    is_behind = A_pos[2] > B_pos[2]


    question_template = random.choice(template_questions)
    response_template = random.choice(true_responses if is_behind else false_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def front_predicate(A, B):
    template_questions = front_predicate_questions
    true_responses = front_true
    false_responses = front_false

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]
    is_in_front = A_pos[2] < B_pos[2]

    question_template = random.choice(template_questions)
    response_template = random.choice(
        true_responses if is_in_front else false_responses
    )

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = response_template.replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def left_tfqa(A, B):
    template_questions = left_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    is_left = A_pos[0] < B_pos[0]  # Compare X coordinates

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_left else 'B.No'

    return question + " Answer: " + answer

def right_tfqa(A, B):
    template_questions = right_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    is_right = A_pos[0] > B_pos[0]  # Compare X coordinates

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_right else 'B.No'

    return question + " Answer: " + answer



def above_tfqa(A, B):
    template_questions = above_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    is_above = A_pos[1] < B_pos[1]

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_above else 'B.No'

    return question + " Answer: " + answer


def below_tfqa(A, B):
    template_questions = below_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    is_below = A_pos[1] > B_pos[1]

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_below else 'B.No'

    return question + " Answer: " + answer

def behind_tfqa(A, B):
    template_questions = behind_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    is_behind = A_pos[2] > B_pos[2]

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_behind else 'B.No'

    return question + " Answer: " + answer


def front_tfqa(A, B):
    template_questions = front_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]
    is_in_front = A_pos[2] < B_pos[2]

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_in_front else 'B.No'

    return question + " Answer: " + answer


def wide_tfqa(A, B):
    template_questions = wide_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    X_A = {point[0] for point in A_bbox}
    X_B = {point[0] for point in B_bbox}

    width_A = abs(max(X_A) - min(X_A))
    width_B = abs(max(X_B) - min(X_B))

    is_wider = width_A > width_B

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_wider else 'B.No'

    return question + " Answer: " + answer


def big_tfqa(A, B):
    template_questions = big_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    X_A = {point[0] for point in A_bbox}
    Y_A = {point[1] for point in A_bbox}
    Z_A = {point[2] for point in A_bbox}

    X_B = {point[0] for point in B_bbox}
    Y_B = {point[1] for point in B_bbox}
    Z_B = {point[2] for point in B_bbox}

    # 计算宽度 (x方向差距), 深度 (y方向差距), 高度 (z方向差距)
    width_A = abs(max(X_A) - min(X_A))
    height_A = abs(max(Y_A) - min(Y_A))
    depth_A = abs(max(Z_A) - min(Z_A))
    volume_A = width_A * depth_A * height_A

    width_B = abs(max(X_B) - min(X_B))
    height_B = abs(max(Y_B) - min(Y_B))
    depth_B = abs(max(Z_B) - min(Z_B))
    volume_B = width_B * depth_B * height_B

    is_bigger = volume_A > volume_B

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_bigger else 'B.No'

    return question + " Answer: " + answer


def tall_tfqa(A, B):
    template_questions = tall_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    Y_A = {point[1] for point in A_bbox}
    Y_B = {point[1] for point in B_bbox}

    height_A = abs(max(Y_A) - min(Y_A))
    height_B = abs(max(Y_B) - min(Y_B))


    is_taller = height_A > height_B

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_taller else 'B.No'

    return question + " Answer: " + answer


def short_tfqa(A, B):
    template_questions = short_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    Y_A = {point[1] for point in A_bbox}
    Y_B = {point[1] for point in B_bbox}

    height_A = abs(max(Y_A) - min(Y_A))
    height_B = abs(max(Y_B) - min(Y_B))


    is_shorter = height_A < height_B

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_shorter else 'B.No'

    return question + " Answer: " + answer


def thin_tfqa(A, B):
    template_questions = thin_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    X_A = {point[0] for point in A_bbox}
    X_B = {point[0] for point in B_bbox}

    width_A = abs(max(X_A) - min(X_A))
    width_B = abs(max(X_B) - min(X_B))

    is_thinner = width_A < width_B

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_thinner else 'B.No'

    return question + " Answer: " + answer


def small_tfqa(A, B):
    template_questions = small_tfqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    X_A = {point[0] for point in A_bbox}
    Y_A = {point[1] for point in A_bbox}
    Z_A = {point[2] for point in A_bbox}

    X_B = {point[0] for point in B_bbox}
    Y_B = {point[1] for point in B_bbox}
    Z_B = {point[2] for point in B_bbox}

    # 计算宽度 (x方向差距), 深度 (y方向差距), 高度 (z方向差距)
    width_A = abs(max(X_A) - min(X_A))
    height_A = abs(max(Y_A) - min(Y_A))
    depth_A = abs(max(Z_A) - min(Z_A))
    volume_A = width_A * depth_A * height_A

    width_B = abs(max(X_B) - min(X_B))
    height_B = abs(max(Y_B) - min(Y_B))
    depth_B = abs(max(Z_B) - min(Z_B))
    volume_B = width_B * depth_B * height_B

    is_smaller = volume_A < volume_B

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = 'A.Yes' if is_smaller else 'B.No'

    return question + " Answer: " + answer



# Choice prompts
def left_choice(A, B):
    template_questions = left_choice_questions
    template_responses = left_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    more_left = A_desc if A_pos[0] < B_pos[0] else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", more_left)

    return question + " Answer: " + answer


def right_choice(A, B):
    template_questions = right_choice_questions
    template_responses = right_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    more_right = A_desc if A_pos[0] > B_pos[0] else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", more_right)

    return question + " Answer: " + answer


def above_choice(A, B):
    template_questions = above_choice_questions
    template_responses = above_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    more_above = A_desc if A_pos[1] < B_pos[1] else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", more_above)

    return question + " Answer: " + answer


def below_choice(A, B):
    template_questions = below_choice_questions
    template_responses = below_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    more_below = A_desc if A_pos[1] > B_pos[1] else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", more_below)

    return question + " Answer: " + answer


def tall_choice(A, B):
    template_questions = tall_choice_questions
    template_responses = tall_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    Y_A = {point[1] for point in A_bbox}
    Y_B = {point[1] for point in B_bbox}

    height_A = abs(max(Y_A) - min(Y_A))
    height_B = abs(max(Y_B) - min(Y_B))

    taller = A_desc if height_A > height_B else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", taller)

    return question + " Answer: " + answer


def short_choice(A, B):
    template_questions = short_choice_questions
    template_responses = short_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    Y_A = {point[1] for point in A_bbox}
    Y_B = {point[1] for point in B_bbox}

    height_A = abs(max(Y_A) - min(Y_A))
    height_B = abs(max(Y_B) - min(Y_B))

    shorter = A_desc if height_A < height_B else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", shorter)

    return question + " Answer: " + answer

def front_choice(A, B):
    template_questions = front_choice_questions
    template_responses = front_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    more_closer = A_desc if A_pos[2] < B_pos[2] else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", more_closer)

    return question + " Answer: " + answer


def behind_choice(A, B):
    template_questions = behind_choice_questions
    template_responses = behind_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    more_further = A_desc if A_pos[2] > B_pos[2] else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", more_further)

    return question + " Answer: " + answer


def wide_choice(A, B):
    template_questions = wide_choice_questions
    template_responses = wide_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    X_A = {point[0] for point in A_bbox}
    X_B = {point[0] for point in B_bbox}

    width_A = abs(max(X_A) - min(X_A))
    width_B = abs(max(X_B) - min(X_B))

    wider = A_desc if width_A > width_B else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", wider)

    return question + " Answer: " + answer


def thin_choice(A, B):
    template_questions = thin_choice_questions
    template_responses = thin_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    X_A = {point[0] for point in A_bbox}
    X_B = {point[0] for point in B_bbox}

    width_A = abs(max(X_A) - min(X_A))
    width_B = abs(max(X_B) - min(X_B))

    thiner = A_desc if width_A < width_B else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", thiner)

    return question + " Answer: " + answer


def big_choice(A, B):
    template_questions = big_choice_questions
    template_responses = big_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    X_A = {point[0] for point in A_bbox}
    Y_A = {point[1] for point in A_bbox}
    Z_A = {point[2] for point in A_bbox}

    X_B = {point[0] for point in B_bbox}
    Y_B = {point[1] for point in B_bbox}
    Z_B = {point[2] for point in B_bbox}

    # 计算宽度 (x方向差距), 深度 (y方向差距), 高度 (z方向差距)
    width_A = abs(max(X_A) - min(X_A))
    height_A = abs(max(Y_A) - min(Y_A))
    depth_A = abs(max(Z_A) - min(Z_A))
    volume_A = width_A * depth_A * height_A

    width_B = abs(max(X_B) - min(X_B))
    height_B = abs(max(Y_B) - min(Y_B))
    depth_B = abs(max(Z_B) - min(Z_B))
    volume_B = width_B * depth_B * height_B

    bigger = A_desc if volume_A > volume_B else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", bigger)

    return question + " Answer: " + answer


def small_choice(A, B):
    template_questions = small_choice_questions
    template_responses = small_choice_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    X_A = {point[0] for point in A_bbox}
    Y_A = {point[1] for point in A_bbox}
    Z_A = {point[2] for point in A_bbox}

    X_B = {point[0] for point in B_bbox}
    Y_B = {point[1] for point in B_bbox}
    Z_B = {point[2] for point in B_bbox}

    # 计算宽度 (x方向差距), 深度 (y方向差距), 高度 (z方向差距)
    width_A = abs(max(X_A) - min(X_A))
    height_A = abs(max(Y_A) - min(Y_A))
    depth_A = abs(max(Z_A) - min(Z_A))
    volume_A = width_A * depth_A * height_A

    width_B = abs(max(X_B) - min(X_B))
    height_B = abs(max(Y_B) - min(Y_B))
    depth_B = abs(max(Z_B) - min(Z_B))
    volume_B = width_B * depth_B * height_B

    smaller = A_desc if volume_A < volume_B else B_desc

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", smaller)

    return question + " Answer: " + answer

def left_multichoice(A, B):
    template_questions = left_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if A_pos[0] < B_pos[0]:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc
    return question + " Answer: " + answer


def right_multichoice(A, B):
    template_questions = right_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if A_pos[0] > B_pos[0]:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc
    return question + " Answer: " + answer


def above_multichoice(A, B):
    template_questions = above_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if A_pos[1] < B_pos[1]:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc
    return question + " Answer: " + answer


def below_multichoice(A, B):
    template_questions = below_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if A_pos[1] > B_pos[1]:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc
    return question + " Answer: " + answer

def front_multichoice(A, B):
    template_questions = front_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]


    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if A_pos[2] < B_pos[2]:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc

    return question + " Answer: " + answer


def behind_multichoice(A, B):
    template_questions = behind_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if A_pos[2] < B_pos[2]:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc

    return question + " Answer: " + answer


def tall_multichoice(A, B):
    template_questions = tall_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    Y_A = {point[1] for point in A_bbox}
    Y_B = {point[1] for point in B_bbox}

    height_A = abs(max(Y_A) - min(Y_A))
    height_B = abs(max(Y_B) - min(Y_B))

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if height_A > height_B:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc

    return question + " Answer: " + answer


def short_multichoice(A, B):
    template_questions = short_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    Y_A = {point[1] for point in A_bbox}
    Y_B = {point[1] for point in B_bbox}

    height_A = abs(max(Y_A) - min(Y_A))
    height_B = abs(max(Y_B) - min(Y_B))

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if height_A < height_B:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc

    return question + " Answer: " + answer

def wide_multichoice(A, B):
    template_questions = wide_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    X_A = {point[0] for point in A_bbox}
    X_B = {point[0] for point in B_bbox}

    width_A = abs(max(X_A) - min(X_A))
    width_B = abs(max(X_B) - min(X_B))


    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if width_A > width_B:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc

    return question + " Answer: " + answer


def thin_multichoice(A, B):
    template_questions = thin_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    X_A = {point[0] for point in A_bbox}
    X_B = {point[0] for point in B_bbox}

    width_A = abs(max(X_A) - min(X_A))
    width_B = abs(max(X_B) - min(X_B))


    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if width_A < width_B:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc

    return question + " Answer: " + answer


def big_multichoice(A, B):
    template_questions = big_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    X_A = {point[0] for point in A_bbox}
    Y_A = {point[1] for point in A_bbox}
    Z_A = {point[2] for point in A_bbox}

    X_B = {point[0] for point in B_bbox}
    Y_B = {point[1] for point in B_bbox}
    Z_B = {point[2] for point in B_bbox}

    # 计算宽度 (x方向差距), 深度 (y方向差距), 高度 (z方向差距)
    width_A = abs(max(X_A) - min(X_A))
    height_A = abs(max(Y_A) - min(Y_A))
    depth_A = abs(max(Z_A) - min(Z_A))
    volume_A = width_A * depth_A * height_A

    width_B = abs(max(X_B) - min(X_B))
    height_B = abs(max(Y_B) - min(Y_B))
    depth_B = abs(max(Z_B) - min(Z_B))
    volume_B = width_B * depth_B * height_B


    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if volume_A > volume_B:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc

    return question + " Answer: " + answer


def small_multichoice(A, B):
    template_questions = small_multiqa_questions

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]
    B_bbox = B["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    X_A = {point[0] for point in A_bbox}
    Y_A = {point[1] for point in A_bbox}
    Z_A = {point[2] for point in A_bbox}

    X_B = {point[0] for point in B_bbox}
    Y_B = {point[1] for point in B_bbox}
    Z_B = {point[2] for point in B_bbox}

    # 计算宽度 (x方向差距), 深度 (y方向差距), 高度 (z方向差距)
    width_A = abs(max(X_A) - min(X_A))
    height_A = abs(max(Y_A) - min(Y_A))
    depth_A = abs(max(Z_A) - min(Z_A))
    volume_A = width_A * depth_A * height_A

    width_B = abs(max(X_B) - min(X_B))
    height_B = abs(max(Y_B) - min(Y_B))
    depth_B = abs(max(Z_B) - min(Z_B))
    volume_B = width_B * depth_B * height_B

    question_template = random.choice(template_questions)
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    if volume_A < volume_B:
        answer = 'A.' + A_desc
    else:
        answer = 'B.' + B_desc

    return question + " Answer: " + answer

# Distance prompts

def generate_spatial_reasoning_data(
        A, B, human_readable_dist, template_questions, template_answers
):
    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()


    question_template = random.choice(template_questions)
    answer_template = random.choice(template_answers)

    # Replace placeholders with actual values
    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = (
        answer_template.replace("[A]", A_desc)
        .replace("[B]", B_desc)
        .replace("[X]", human_readable_dist)
    )

    # Add to the dataset
    return question + " Answer: " + answer


def distance_data(A, B):
    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]
    distance = math.sqrt((A_pos[0] - B_pos[0]) ** 2 +
                         (A_pos[1] - B_pos[1]) ** 2 +
                         (A_pos[2] - B_pos[2]) ** 2)
    human_readable_dist = human_like_distance(distance)
    return generate_spatial_reasoning_data(A, B, human_readable_dist, distance_template_questions, distance_template_answers)


def vertical_distance_data(A, B):
    template_questions = vertical_distance_questions
    template_answers = vertical_distance_answers

    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]
    vertical_distance = abs(A_pos[1] - B_pos[1])
    human_readable_dist = human_like_distance(vertical_distance)

    return generate_spatial_reasoning_data(
        A, B, human_readable_dist, template_questions, template_answers
    )


def horizontal_distance_data(A, B):
    template_questions = horizontal_distance_questions
    template_answers = horizontal_distance_answers

    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]
    horizontal_distance = np.sqrt((A_pos[0] - B_pos[0]) ** 2)

    human_readable_dist = human_like_distance(horizontal_distance)
    return generate_spatial_reasoning_data(
        A, B, human_readable_dist, template_questions, template_answers
    )


def width_data(A, B=None):
    template_questions = width_questions
    template_answers = width_answers

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    X_A = {point[0] for point in A_bbox}

    # 计算宽度 (x方向差距), 深度 (y方向差距), 高度 (z方向差距)
    width_A = abs(max(X_A) - min(X_A))
    human_readable_width = human_like_distance(width_A)

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_answers)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc).replace("[X]", human_readable_width)

    return question + " Answer: " + answer


def height_data(A, B=None):
    template_questions = height_questions
    template_answers = height_answers

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    Y_A = {point[1] for point in A_bbox}
    height_A = abs(max(Y_A) - min(Y_A))
    human_readable_height = human_like_distance(height_A)

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_answers)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc).replace("[X]", human_readable_height)

    return question + " Answer: " + answer


def human_like_volume(volume):
    if volume < 0.001:
        human_read_volume = round(volume * 1000, 2)
        return f"{volume} cubic decimeter"
    else:
        human_read_volume = round(volume, 2)
        return f"{volume} cubic meter"


def volume_data(A, B=None):

    template_questions = volume_questions
    template_answers = volume_answers

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()

    # 获取A,B bbox
    A_bbox = A["cam_bbox_3d"]

    # 提取唯一的 x, y, z 坐标值
    X_A = {point[0] for point in A_bbox}
    Y_A = {point[1] for point in A_bbox}
    Z_A = {point[2] for point in A_bbox}


    # 计算宽度 (x方向差距), 深度 (y方向差距), 高度 (z方向差距)
    width_A = abs(max(X_A) - min(X_A))
    height_A = abs(max(Y_A) - min(Y_A))
    depth_A = abs(max(Z_A) - min(Z_A))
    volume_A = width_A * depth_A * height_A

    human_readable_volume = human_like_volume(volume_A)

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_answers)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc).replace("[X]", human_readable_volume)

    return question + " Answer: " + answer





def angle_data(A, B):
    template_questions = angle_questions
    template_answers = angle_answers

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    # 计算从A到B的方向角
    delta_x = B_pos[0] - A_pos[0]
    delta_z = B_pos[2] - A_pos[2]
    angle_rad = math.atan2(delta_x, delta_z)  # 反正切函数计算角度
    angle_degrees = math.degrees(angle_rad)
    angle_degrees = round(angle_degrees, 2)

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_answers)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[A]", A_desc).replace("[B]", B_desc).replace("[X]", str(angle_degrees))

    return question + " Answer: " + answer


def direction_data(A, B):
    template_questions = direction_questions
    template_responses = direction_answers

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    B_desc = B["cropped_image_info"]["cropped_image_caption"]
    A_desc, B_desc = A_desc.lower(), B_desc.lower()

    # 获取A,B坐标，他们是列表
    A_pos = A["cam_obj_loc"][0]
    B_pos = B["cam_obj_loc"][0]

    # 计算从A到B的方向角
    delta_x = B_pos[0] - A_pos[0]
    delta_z = B_pos[2] - A_pos[2]

    angle_rad = math.atan2(delta_x, delta_z)  # 反正切函数计算角度
    angle_degrees = math.degrees(angle_rad)
    angle_degrees = round(angle_degrees, 2)
    angle_degrees = (angle_degrees + 360) % 360
    clock_position = (12 + angle_degrees // 30) % 12
    clock_position = clock_position if clock_position > 0 else 12 + clock_position

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc).replace("[B]", B_desc)
    answer = answer_template.replace("[X]", str(int(clock_position))).replace("[A]", A_desc).replace("[B]", B_desc)

    return question + " Answer: " + answer


def angle2agent(A, B=None):
    template_questions = angle2agent_questions
    template_responses = angle2agent_answers

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()
    A_pos = A["cam_obj_loc"][0]

    angle_rad = math.atan2(A_pos[0], A_pos[2])  # 反正切函数计算角度
    angle_degrees = math.degrees(angle_rad)
    angle_degrees = round(angle_degrees, 2)

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc).replace("[X]", str(angle_degrees))

    return question + " Answer: " + answer


def direction2agent(A, B=None):
    template_questions = direction2agent_questions
    template_responses = direction2agent_answers

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()
    A_pos = A["cam_obj_loc"][0]

    angle_rad = math.atan2(A_pos[0], A_pos[2])  # 反正切函数计算角度
    angle_degrees = math.degrees(angle_rad)
    angle_degrees = round(angle_degrees, 2)

    angle_degrees = (angle_degrees + 360) % 360
    clock_position = (12 + angle_degrees // 30) % 12
    clock_position = clock_position if clock_position > 0 else 12 + clock_position

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc).replace("[X]", str(int(clock_position)))

    return question + " Answer: " + answer


def distance2agent(A, B=None):
    template_questions = distance2agent_questions
    template_responses = distance2agent_answers

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()
    A_pos = A["cam_obj_loc"][0]

    distance = np.linalg.norm(A_pos)
    human_like_dist = human_like_distance(distance)

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc).replace("[X]", human_like_dist)
    return question + " Answer: " + answer


def vertical_distance2agent(A, B=None):
    template_questions = vertical_distance2agent_questions
    template_responses = vertical_distance2agent_answers

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()
    A_pos = A["cam_obj_loc"][0]

    vertical_distance = abs(A_pos[1])
    human_like_dist = human_like_distance(vertical_distance)

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc).replace("[X]", human_like_dist)
    return question + " Answer: " + answer


def horizontal_distance2agent(A, B=None):
    template_questions = horizontal_distance2agent_questions
    template_responses = horizontal_distance2agent_answers

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()
    A_pos = A["cam_obj_loc"][0]

    horizontal_distance = abs(A_pos[0])
    human_like_dist = human_like_distance(horizontal_distance)

    question_template = random.choice(template_questions)
    answer_template = random.choice(template_responses)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc).replace("[X]", human_like_dist)
    return question + " Answer: " + answer


def left_relationship2agent(A, B=None):
    template_questions = left2agent_questions
    true_responses = left2agent_true_responses
    false_responses = left2agent_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()
    A_pos = A["cam_obj_loc"][0]

    is_left = A_pos[0] < 0

    question_template = random.choice(template_questions)
    answer_template = random.choice(true_responses if is_left else false_responses)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc)
    return question + " Answer: " + answer


def right_relationship2agent(A, B=None):
    template_questions = right2agent_questions
    true_responses = right2agent_true_responses
    false_responses = right2agent_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()
    A_pos = A["cam_obj_loc"][0]

    is_right = A_pos[0] > 0

    question_template = random.choice(template_questions)
    answer_template = random.choice(true_responses if is_right else false_responses)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc)
    return question + " Answer: " + answer


def above_relationship2agent(A, B=None):
    template_questions = above2agent_questions
    true_responses = above2agent_true_responses
    false_responses = above2agent_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()
    A_pos = A["cam_obj_loc"][0]

    is_above = A_pos[1] < 0

    question_template = random.choice(template_questions)
    answer_template = random.choice(true_responses if is_above else false_responses)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc)
    return question + " Answer: " + answer


def below_relationship2agent(A, B=None):
    template_questions = below2agent_questions
    true_responses = below2agent_true_responses
    false_responses = below2agent_false_responses

    A_desc = A["cropped_image_info"]["cropped_image_caption"]
    A_desc = A_desc.lower()
    A_pos = A["cam_obj_loc"][0]

    is_below = A_pos[1] > 0

    question_template = random.choice(template_questions)
    answer_template = random.choice(true_responses if is_below else false_responses)

    question = question_template.replace("[A]", A_desc)
    answer = answer_template.replace("[A]", A_desc)
    return question + " Answer: " + answer


def evaluate_predicates_on_pairs(pairs):
    qualitative_prompts = [
        # Spatial relationship predicate_prompts
        left_predicate,
        right_predicate,
        above_predicate,
        below_predicate,
        front_predicate,
        behind_predicate,
        # Spatial relationship choice_prompts
        left_choice,
        right_choice,
        above_choice,
        below_choice,
        front_choice,
        behind_choice,

        # Objects recognition predicate_prompts
        big_predicate,
        small_predicate,
        wide_predicate,
        thin_predicate,
        tall_predicate,
        short_predicate,

        # Objects recognition choice_prompts
        big_choice,
        small_choice,
        wide_choice,
        thin_choice,
        tall_choice,
        short_choice,
    ]
    multi_qa_prompts = [
        left_multichoice,
        right_multichoice,
        above_multichoice,
        below_multichoice,
        front_multichoice,
        behind_multichoice,

        # Objects recognition choice_prompts
        big_multichoice,
        small_multichoice,
        wide_multichoice,
        thin_multichoice,
        tall_multichoice,
        short_multichoice,
    ]
    tf_qa_prompts = [
        left_tfqa,
        right_tfqa,
        above_tfqa,
        below_tfqa,
        front_tfqa,
        behind_tfqa,

        # Objects attribute tf_prompts
        big_tfqa,
        small_tfqa,
        wide_tfqa,
        thin_tfqa,
        tall_tfqa,
        short_tfqa,
    ]
    quantitative_prompts = [
        # Objects recognition data_prompts
        width_data,
        height_data,
        volume_data,
        # Spatial distance data_prompts
        distance_data,
        vertical_distance_data,
        horizontal_distance_data,
        # Spatial angle data_prompts
        # angle_data,
        direction_data,
    ]
    embodied_prompts = [
        # Embodied Spatial relationship predict_prompts
        left_relationship2agent,
        right_relationship2agent,
        above_relationship2agent,
        below_relationship2agent,

        # Embodied Spatial distance data_prompts
        distance2agent,
        vertical_distance2agent,
        horizontal_distance2agent,
        # Embodied Spatial angle data_prompts
        # angle2agent,
        direction2agent,
    ]

    # all_prompt_variants = qualitative_prompts + quantitative_prompts
    # all_prompt_variants = qualitative_prompts + quantitative_prompts + embodied_prompts
    all_prompt_variants = multi_qa_prompts + tf_qa_prompts
    results = []
    qa_information = []

    for A, B in pairs:
        pair_qa_results = []
        pair_qa_info = []
        for prompt_func in all_prompt_variants:
            # for prompt_func in selected_prompt_choices:
            pair_qa_info.append(prompt_func.__name__)
            pair_qa_results.append(prompt_func(A, B))
        results.extend(pair_qa_results)
        qa_information.extend(pair_qa_info)
    return results, qa_information
