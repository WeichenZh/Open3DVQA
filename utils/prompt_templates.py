# Distance
distance_template_questions = [
    "What is the distance between the [A] and the [B]?",
    "How far apart are the [A] and the [B]?",
    "How distant is the [A] from the [B]?",
    "How far is the [A] from the [B]?",
    "How close is the [A] from the [B]?",
    "Could you measure the distance between the [A] and the [B]?",
    "Can you tell me the distance of the [A] from the [B]?",
    "How far away is the [A] from the [B]?",
    "Can you provide the distance measurement between the [A] and the [B]?",
    "Can you give me an estimation of the distance between the [A] and the [B]?",
    "Could you provide the distance between the [A] and the [B]?",
    "How much distance is there between the [A] and the [B]?",
    "Tell me the distance between the [A] and the [B].",
    "Give me the distance from the [A] to the [B].",
    "Measure the distance from the [A] to the [B].",
    "Measure the distance between the [A] and the [B].",
]

distance_template_answers = [
    "[X]",
    "The [A] and the [B] are [X] apart.",
    "The [A] is [X] away from the [B].",
    "A distance of [X] exists between the [A] and the [B].",
    "The [A] is [X] from the [B].",
    "The [A] and the [B] are [X] apart from each other.",
    "They are [X] apart.",
    "The distance of the [A] from the [B] is [X].",
]

# Predicates
left_predicate_questions = [
    "Is the [A] to the left of the [B] from the viewer's perspective?",
    "Does the [A] appear on the left side of the [B]?",
    "Can you confirm if the [A] is positioned to the left of the [B]?",
]

left_true_responses = [
    "Yes, the [A] is to the left of the [B].",
    "Indeed, the [A] is positioned on the left side of the [B].",
    "Correct, you'll find the [A] to the left of the [B].",
]

left_false_responses = [
    "No, the [A] is not to the left of the [B].",
    "In fact, the [A] is either to the right of or directly aligned with the [B].",
    "Incorrect, the [A] is not on the left side of the [B].",
]

right_predicate_questions = [
    "Is the [A] to the right of the [B] from the viewer's perspective?",
    "Does the [A] appear on the right side of the [B]?",
    "Can you confirm if the [A] is positioned to the right of the [B]?",
]

right_true_responses = [
    "Yes, the [A] is to the right of the [B].",
    "Indeed, the [A] is positioned on the right side of the [B].",
    "Correct, you'll find the [A] to the right of the [B].",
]

right_false_responses = [
    "No, the [A] is not to the right of the [B].",
    "In fact, the [A] is either to the left of or directly aligned with the [B].",
    "Incorrect, the [A] is not on the right side of the [B].",
]

above_predicate_questions = [
    "Is the [A] above the [B]?",
    "Does the [A] appear over the [B]?",
    "Can you confirm if the [A] is positioned above the [B]?",
]

above_true_responses = [
    "Yes, the [A] is above the [B].",
    "Indeed, the [A] is positioned over the [B].",
    "Correct, the [A] is located above the [B].",
]

above_false_responses = [
    "No, the [A] is not above the [B].",
    "Actually, the [A] is either below or at the same elevation as the [B].",
    "Incorrect, the [A] is not positioned above the [B].",
]

below_predicate_questions = [
    "Is the [A] below the [B]?",
    "Does the [A] appear under the [B]?",
    "Can you confirm if the [A] is positioned below the [B]?",
]

below_true_responses = [
    "Yes, the [A] is below the [B].",
    "Indeed, the [A] is positioned under the [B].",
    "Correct, the [A] is located below the [B].",
]

below_false_responses = [
    "No, the [A] is not below the [B].",
    "Actually, the [A] is either above or at the same elevation as the [B].",
    "Incorrect, the [A] is not positioned below the [B].",
]

wide_predicate_questions = [
    "Is the [A] wider than the [B]?",
    "Does the [A] have a greater width compared to the [B]?",
    "Can you confirm if the [A] is wider than the [B]?",
]

wide_true_responses = [
    "Yes, the [A] is wider than the [B].",
    "Indeed, the [A] has a greater width compared to the [B].",
    "Correct, the width of the [A] exceeds that of the [B].",
]

wide_false_responses = [
    "No, the [A] is not wider than the [B].",
    "In fact, the [A] might be narrower or the same width as the [B].",
    "Incorrect, the [A]'s width does not surpass the [B]'s.",
]

big_predicate_questions = [
    "Is the [A] bigger than the [B]?",
    "Does the [A] have a larger size compared to the [B]?",
    "Can you confirm if the [A] is bigger than the [B]?",
]

big_true_responses = [
    "Yes, the [A] is bigger than the [B].",
    "Indeed, the [A] has a larger size compared to the [B].",
    "Correct, the [A] is larger in size than the [B].",
]

big_false_responses = [
    "No, the [A] is not bigger than the [B].",
    "Actually, the [A] might be smaller or the same size as the [B].",
    "Incorrect, the [A] is not larger than the [B].",
]

tall_predicate_questions = [
    "Is the [A] taller than the [B]?",
    "Does the [A] have a greater height compared to the [B]?",
    "Can you confirm if the [A] is taller than the [B]?",
]

tall_true_responses = [
    "Yes, the [A] is taller than the [B].",
    "Indeed, the [A] has a greater height compared to the [B].",
    "Correct, the [A] is much taller as the [B].",
]

tall_false_responses = [
    "No, the [A] is not taller than the [B].",
    "In fact, the [A] may be shorter or the same height as the [B].",
    "Incorrect, the [A]'s height is not larger of the [B]'s.",
]

short_predicate_questions = [
    "Is the [A] shorter than the [B]?",
    "Does the [A] have a lesser height compared to the [B]?",
    "Can you confirm if the [A] is shorter than the [B]?",
]

short_true_responses = [
    "Yes, the [A] is shorter than the [B].",
    "Indeed, the [A] has a lesser height compared to the [B].",
    "Correct, the [A] is not as tall as the [B].",
]

short_false_responses = [
    "No, the [A] is not shorter than the [B].",
    "In fact, the [A] may be taller or the same height as the [B].",
    "Incorrect, the [A]'s height does not fall short of the [B]'s.",
]

thin_predicate_questions = [
    "Is the [A] thinner than the [B]?",
    "Does the [A] have a lesser width compared to the [B]?",
    "Can you confirm if the [A] is thinner than the [B]?",
]

thin_true_responses = [
    "Yes, the [A] is thinner than the [B].",
    "Indeed, the [A] has a lesser width compared to the [B].",
    "Correct, the [A]'s width is less than the [B]'s.",
]

thin_false_responses = [
    "No, the [A] is not thinner than the [B].",
    "In fact, the [A] might be wider or the same width as the [B].",
    "Incorrect, the [A]'s width is not less than the [B]'s.",
]

small_predicate_questions = [
    "Is the [A] smaller than the [B]?",
    "Does the [A] have a smaller size compared to the [B]?",
    "Can you confirm if the [A] is smaller than the [B]?",
]

small_true_responses = [
    "Yes, the [A] is smaller than the [B].",
    "Indeed, the [A] has a smaller size compared to the [B].",
    "Correct, the [A] occupies less space than the [B].",
]

small_false_responses = [
    "No, the [A] is not smaller than the [B].",
    "Actually, the [A] might be larger or the same size as the [B].",
    "Incorrect, the [A] is not smaller in size than the [B].",
]

behind_predicate_questions = [
    "Is the [A] behind the [B]?",
    "Is the position of the [A] more distant than that of the [B]?",
    "Does the [A] lie behind the [B]?",
    "Is the [A] positioned behind the [B]?",
    "Is the [A] further to camera compared to the [B]?",
    "Does the [A] come behind the [B]?",
    "Is the [A] positioned at the back of the [B]?",
    "Is the [A] further to the viewer compared to the [B]?",
]

behind_true = [
    "Yes.",
    "Yes, it is.",
    "Yes, it is behind the [B].",
    "That is True.",
    "Yes, the [A] is further from the viewer.",
    "Yes, the [A] is behind the [B].",
]

behind_false = [
    "No.",
    "No, it is not.",
    "No, it is in front of the [B].",
    "That is False.",
    "No, the [A] is closer to the viewer.",
    "No, the [B] is in front of the [A].",
]

front_predicate_questions = [
    "Is the [A] in front of the [B]?",
    "Is the position of the [A] less distant than that of the [B]?",
    "Does the [A] lie in front of the [B]?",
    "Is the [A] positioned in front of the [B]?",
    "Is the [A] closer to camera compared to the [B]?",
    "Does the [A] come in front of the [B]?",
    "Is the [A] positioned before the [B]?",
    "Is the [A] closer to the viewer compared to the [B]?",
]

front_true = [
    "Yes.",
    "Yes, it is.",
    "Yes, it is in front of the [B].",
    "That is True.",
    "Yes, the [A] is closer to the viewer.",
    "Yes, the [A] is in front of the [B].",
]

front_false = [
    "No.",
    "No, it is not.",
    "No, it is behind the [B].",
    "That is False.",
    "No, the [A] is further to the viewer.",
    "No, the [B] is behind the [A].",
]


# Choice
left_choice_questions = [
    "Which is more to the left, the [A] or the [B]?",
    "Between the [A] and the [B], which one appears on the left side from the viewer's perspective?",
    "Who is positioned more to the left, the [A] or the [B]?",
]

left_choice_responses = [
    "[X] is more to the left.",
    "From the viewer's perspective, [X] appears more on the left side.",
    "Positioned to the left is [X].",
]

right_choice_questions = [
    "Which is more to the right, the [A] or the [B]?",
    "Between the [A] and the [B], which one appears on the right side from the viewer's perspective?",
    "Who is positioned more to the right, the [A] or the [B]?",
]

right_choice_responses = [
    "[X] is more to the right.",
    "From the viewer's perspective, [X] appears more on the right side.",
    "Positioned to the right is [X].",
]

above_choice_questions = [
    "Which is above, the [A] or the [B]?",
    "Between the [A] and the [B], which one is positioned higher?",
    "Who is higher up, the [A] or the [B]?",
]

above_choice_responses = [
    "[X] is above.",
    "Positioned higher is [X].",
    "[X] is higher up.",
]

below_choice_questions = [
    "Which is below, the [A] or the [B]?",
    "Between the [A] and the [B], which one is positioned lower?",
    "Who is lower down, the [A] or the [B]?",
]

below_choice_responses = [
    "[X] is below.",
    "Positioned lower is [X].",
    "[X] is lower down.",
]

tall_choice_questions = [
    "Who is taller, the [A] or the [B]?",
    "Between the [A] and the [B], which one has more height?",
    "Which of these two, the [A] or the [B], stands taller?",
]

tall_choice_responses = [
    "[X] is taller.",
    "With more height is [X].",
    "Standing taller between the two is [X].",
]

short_choice_questions = [
    "Who is shorter, the [A] or the [B]?",
    "Between the [A] and the [B], which one has less height?",
    "Which of these two, the [A] or the [B], stands shorter?",
]

short_choice_responses = [
    "[X] is shorter.",
    "With less height is [X].",
    "Standing shorter between the two is [X].",
]


# Vertical and horizontal distance
vertical_distance_questions = [
    "What is the vertical distance between the [A] and the [B]?",
    "How far apart are the [A] and the [B] vertically?",
    "How distant is the [A] from the [B] vertically?",
    "How far is the [A] from the [B] vertically?",
    "Could you measure the vertical distance between the [A] and the [B]?",
    "Can you tell me the vertical distance between the [A] and the [B]?",
    "How far away is the [A] from the [B] vertically?",
    "Estimate the vertical distance between the [A] and the [B].",
    "Could you provide the vertical distance between the [A] and the [B]?",
    "How much distance is there between the [A] and the [B] vertically?",
    "Tell me the distance between the [A] and the [B] vertically.",
    "Give me the vertical distance from the [A] to the [B].",
    "Measure the vertical distance from the [A] to the [B].",
    "Measure the distance between the [A] and the [B] vertically.",
]

vertical_distance_answers = [
    "[X]",
    "The [A] and the [B] are [X] apart vertically.",
    "The [A] is [X] away from the [B] vertically.",
    "A vertical distance of [X] exists between the [A] and the [B].",
    "The [A] is [X] from the [B] vertically.",
    "The [A] and the [B] are [X] apart vertically from each other.",
    "Vertically, They are [X] apart.",
    "The vertical distance of the [A] from the [B] is [X].",
    "They are [X] apart.",
    "It is approximately [X].",
]

horizontal_distance_questions = [
    "What is the horizontal distance between the [A] and the [B]?",
    "How far apart are the [A] and the [B] horizontally?",
    "How distant is the [A] from the [B] horizontally?",
    "How far is the [A] from the [B] horizontally?",
    "Could you measure the horizontal distance between the [A] and the [B]?",
    "Can you tell me the horizontal distance of the [A] from the [B]?",
    "Can you give me an estimation of the horizontal distance between the [A]"
    " and the [B]?"
    "Could you provide the horizontal distance between the [A] and the [B]?",
    "How much distance is there between the [A] and the [B] horizontally?",
    "Tell me the distance between the [A] and the [B] horizontally.",
    "Give me the horizontal distance from the [A] to the [B].",
    "Vertial gap between the [A] and the [B].",
    "Measure the horizontal distance from the [A] to the [B].",
    "Measure the distance between the [A] and the [B] horizontally.",
]

horizontal_distance_answers = [
    "[X]",
    "The [A] and the [B] are [X] apart horizontally.",
    "The [A] is [X] away from the [B] horizontally.",
    "A horizontal distance of [X] exists between the [A] and the [B].",
    "The [A] is [X] from the [B] horizontally.",
    "The [A] and the [B] are [X] apart horizontally from each other.",
    "Horizontally, They are [X] apart.",
    "The horizontal distance of the [A] from the [B] is [X].",
    "They are [X] apart.",
    "It is approximately [X].",
]

# Width/Height
width_questions = [
    "Measure the width of the [A].",
    "Determine the horizontal dimensions of the [A].",
    "Find out how wide the [A] is.",
    "What is the width of the [A]?",
    "How wide is the [A]?",
    "What are the dimensions of the [A] in terms of width?",
    "Could you tell me the horizontal size of the [A]?",
    "What is the approximate width of the [A]?",
    "How wide is the [A]?",
    "How much space does the [A] occupy horizontally?",
    "How big is the [A]?",
    "How big is the [A] in terms of width?",
    "What is the radius of the [A]?",
]
width_answers = [
    "[X]",
    "The width of the [A] is [X].",
    "the [A] is [X] wide.",
    "the [A] is [X] in width.",
    "It is [X].",
]

height_questions = [
    "Measure the height of the [A].",
    "Determine the vertical dimensions of the [A].",
    "Find out how tall the [A] is.",
    "What is the height of the [A]?",
    "How tall is the [A]?",
    "What are the dimensions of the [A] in terms of height?",
    "Could you tell me the vericall size of the [A]?",
    "What is the approximate height of the [A]?",
    "How tall is the [A]?",
    "How much space does the [A] occupy vertically?",
    "How tall is the [A]?",
    "How tall is the [A] in terms of width?",
]
height_answers = [
    "[X]",
    "The height of the [A] is [X].",
    "the [A] is [X] tall.",
    "the [A] is [X] in height.",
    "It is [X].",
]

volume_questions = [
    "Measure the volume of the [A].",
    "Determine the total volume of the [A].",
    "Find out the volume of the [A].",
    "What is the volume of the [A]?",
    "How much space does the [A] occupy?",
    "What is the capacity of the [A]?",
    "Could you tell me the volume of the [A]?",
    "What is the approximate volume of the [A]?",
    "How much volume does the [A] have?",
    "What is the total volume of the [A]?",
    "How much space does the [A] take up?",
]

volume_answers = [
    "[X]",
    "The volume of the [A] is [X].",
    "The [A] has a volume of [X].",
]

angle_questions = [
    "What is the angle of the [B] relative to the [A]?",
    "How large is the angle of the [B] in relation to the [A]?",
    "Can you measure the angle of the [B] with respect to the [A]?",
    "How many degrees is the angle of the [B] relative to the [A]?",
    "What is the degree of the angle of the [B] in relation to the [A]?",
    "How much is the angle of the [B] compared to the [A]?",
    "Could you provide the angle of the [B] relative to the [A]?",
    "Tell me the angle of the [B] compared to the [A].",
    "Estimate the angle of the [B] with respect to the [A].",
    "Could you measure the angle of the [B] relative to the [A]?",
    "Give me the angle of the [B] relative to the [A].",
    "What is the angle of the [B] when viewed from the [A]?",
    "Measure the angle of the [B] relative to the [A].",
    "How wide is the angle of the [B] compared to the [A]?",
]

angle_answers = [
    "[X] degrees.",
    "The angle of the [B] as seen from the [A] is [X] degrees.",
    "The [B] forms an angle of [X] degrees when viewed from the [A].",
    "The [B] is positioned at an angle of [X] degrees relative to the [A].",
    "The angle of the [B] with respect to the [A] is [X] degrees.",
    "An angle of [X] degrees exists from the [A]'s perspective towards the [B].",
    "The relative angle of the [B] when viewed from the [A] is [X] degrees.",
    "The angle as observed from the [A] is approximately [X] degrees.",
]

front_choice_questions = [
    "Which is closer to viewer, the [A] or the [B]?",
    "Between the [A] and the [B], which one appears on closer from the viewer's perspective?",
    "Who is positioned closer to viewer, the [A] or the [B]?",
]

front_choice_responses = [
    "[X] is more closer to the viewer.",
    "From the viewer's perspective, [X] appears closer.",
    "Positioned to the closer is [X].",
]

behind_choice_questions = [
    "Which is further to viewer, the [A] or the [B]?",
    "Between the [A] and the [B], which one appears on further to the viewer's perspective?",
    "Who is positioned further to viewer, the [A] or the [B]?",
]

behind_choice_responses = [
    "[X] is further to the viewer.",
    "From the viewer's perspective, [X] appears further.",
    "Positioned to the further is [X].",
]

wide_choice_questions = [
    "Who is wider, the [A] or the [B]?",
    "Between the [A] and the [B], which one has more width?",
    "Which of these two, the [A] or the [B], appears wider?",
]

wide_choice_responses = [
    "[X] is wider.",
    "With more width is [X].",
    "Appearing wider between the two is [X].",
]

thin_choice_questions = [
    "Who is thinner, the [A] or the [B]?",
    "Between the [A] and the [B], which one has less width?",
    "Which of these two, the [A] or the [B], appears thinner?",
]

thin_choice_responses = [
    "[X] is thinner.",
    "With less width is [X].",
    "Appearing thinner between the two is [X].",
]

big_choice_questions = [
    "Who is bigger, the [A] or the [B]?",
    "Between the [A] and the [B], which one has more volume?",
    "Which of these two, the [A] or the [B], appears bigger?",
]

big_choice_responses = [
    "[X] is bigger.",
    "With more volume is [X].",
    "Appearing bigger between the two is [X].",
]

small_choice_questions = [
    "Who is smaller, the [A] or the [B]?",
    "Between the [A] and the [B], which one has less volume?",
    "Which of these two, the [A] or the [B], appears smaller?",
]

small_choice_responses = [
    "[X] is smaller.",
    "With less volume is [X].",
    "Appearing smaller between the two is [X].",
]


# embodied tasks
distance2agent_questions = [
    "What is the distance between the [A] and you?",
    "How far apart are the [A] and you?",
    "How distant is the [A] from you?",
    "How far is the [A] from you?",
    "How close is the [A] from you?",
    "Could you measure the distance between the [A] and you?",
    "Can you tell me the distance of the [A] from you?",
    "How far away is the [A] from you?",
    "Can you provide the distance measurement between the [A] and you?",
    "Can you give me an estimation of the distance between the [A] and you?",
    "Could you provide the distance between the [A] and you?",
    "How much distance is there between the [A] and you?",
    "Tell me the distance between the [A] and you.",
    "Give me the distance from the [A] to you.",
    "Measure the distance from the [A] to you.",
    "Measure the distance between the [A] and you.",
]

distance2agent_answers = [
    "[X]",
    "The [A] is [X] away.",
    "A distance of [X] exists.",
    "The distance of the [A] is [X].",
]

vertical_distance2agent_questions = [
    "What is the vertical distance between the [A] and you?",
    "How far apart are the [A] and you vertically?",
    "How distant is the [A] from you vertically?",
    "How far is the [A] from you vertically?",
    "Could you measure the vertical distance between the [A] and you?",
    "Can you tell me the vertical distance between the [A] and you?",
    "How far away is the [A] from you vertically?",
    "Estimate the vertical distance between the [A] and you.",
    "Could you provide the vertical distance between the [A] and you?",
    "How much distance is there between the [A] and you vertically?",
    "Tell me the distance between the [A] and you vertically.",
    "Give me the vertical distance from the [A] to you.",
    "Measure the vertical distance from the [A] to you.",
    "Measure the distance between the [A] and you vertically.",
]

vertical_distance2agent_answers = [
    "[X]",
    "The [A] is [X] away vertically.",
    "A vertical distance of [X] exists.",
    "Vertically, [X] apart.",
    "The vertical distance of the [A] is [X].",
    "It is approximately [X].",
]

horizontal_distance2agent_questions = [
    "What is the horizontal distance between the [A] and you?",
    "How far apart are the [A] and you horizontally?",
    "How distant is the [A] from you horizontally?",
    "How far is the [A] from you horizontally?",
    "Could you measure the horizontal distance between the [A] and you?",
    "Can you tell me the horizontal distance of the [A] from you?",
    "Can you give me an estimation of the horizontal distance between the [A]"
    " and you?"
    "Could you provide the horizontal distance between the [A] and you?",
    "How much distance is there between the [A] and you horizontally?",
    "Tell me the distance between the [A] and you horizontally.",
    "Give me the horizontal distance from the [A] to you.",
    "Vertial gap between the [A] and you.",
    "Measure the horizontal distance from the [A] to you.",
    "Measure the distance between the [A] and you horizontally.",
]

horizontal_distance2agent_answers = [
    "[X]",
    "The [A] is [X] apart horizontally.",
    "A horizontal distance of [X] exists.",
    "Horizontally, [X] apart.",
    "The horizontal distance of the [A] is [X].",
    "It is approximately [X].",
]

angle2agent_questions = [
    "What is the angle of [A]?",
    "How large is the angle of [A]?",
    "Can you measure the angle of [A]?",
    "How many degrees is the angle of [A]?",
    "What is the degree of the angle of [A]?",
    "Could you provide the angle of [A]?",
    "Tell me the angle of [A].",
    "Estimate the angle of [A].",
    "Could you measure the angle of [A]?",
    "Give me the angle of [A].",
    "What is the angle of [A]?",
    "Measure the angle of [A].",
]

direction2agent_answers = [
    "[X] o'clock .",
    "[A] is positioned at a direction of [X] o'clock .",
    "The direction of [A] is [X] o'clock .",
    "The direction observed is approximately [X] o'clock .",
]

direction2agent_questions = [
    "What is the direction of [A]?",
    "Can you measure the direction of [A]?",
    "Could you provide the direction of [A]?",
    "Tell me the direction of [A].",
    "Estimate the direction of [A].",
    "Give me the angle of [A].",
    "Measure the direction of [A].",
]

angle2agent_answers = [
    "[X] degrees.",
    "[A] is positioned at an angle of [X] degrees.",
    "The angle of [A] is [X] degrees.",
    "The angle observed is approximately [X] degrees.",
]

# Predicates
left2agent_questions = [
    "Is the [A] to the left of you from the viewer's perspective?",
    "Does the [A] appear on the left side of you?",
    "Can you confirm if the [A] is positioned to the left of you?",
]

left2agent_true_responses = [
    "Yes, the [A] is to the left.",
    "Indeed, the [A] is positioned on the left side.",
    "Correct, you'll find the [A] to the left.",
]

left2agent_false_responses = [
    "No, the [A] is not to the left.",
    "In fact, the [A] is either to the right of or directly.",
    "Incorrect, the [A] is not on the left side",
]

right2agent_questions = [
    "Is the [A] to the right of you from the viewer's perspective?",
    "Does the [A] appear on the right side of you?",
    "Can you confirm if the [A] is positioned to the right of you?",
]

right2agent_true_responses = [
    "Yes, the [A] is to the right.",
    "Indeed, the [A] is positioned on the right side.",
    "Correct, you'll find the [A] to the right.",
]

right2agent_false_responses = [
    "No, the [A] is not to the right.",
    "In fact, the [A] is either to the left of or directly.",
    "Incorrect, the [A] is not on the right side.",
]

above2agent_questions = [
    "Is the [A] above you?",
    "Does the [A] appear over you?",
    "Can you confirm if the [A] is positioned above you?",
]

above2agent_true_responses = [
    "Yes, the [A] is above.",
    "Indeed, the [A] is positioned over.",
    "Correct, the [A] is located above.",
]

above2agent_false_responses = [
    "No, the [A] is not above.",
    "Actually, the [A] is either below or at the same elevation.",
    "Incorrect, the [A] is not positioned above.",
]

below2agent_questions = [
    "Is the [A] below?",
    "Does the [A] appear under?",
    "Can you confirm if the [A] is positioned below",
]

below2agent_true_responses = [
    "Yes, the [A] is below.",
    "Indeed, the [A] is positioned under.",
    "Correct, the [A] is located below.",
]

below2agent_false_responses = [
    "No, the [A] is not below.",
    "Actually, the [A] is either above or at the same elevation.",
    "Incorrect, the [A] is not positioned below.",
]

direction_questions = [
    "If you are at [A], where will you find [B]?"
]

direction_answers = [
    "[B] is roughly at [X] o'clock from [A].",
    "[A] will find [B] around the [X] o'clock direction."
]

