# Building a Multiple Choice Quiz (3:57:38)
from Questions import Questions

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n"
]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "b")]


def run_test(arr_quest):
    score = 0
    for question in arr_quest:
        resp = input(question.prompt)
        if resp == question.answer:
            score += 1

    print("You did " + str(score) + " from " + str(len(arr_quest)))


run_test(questions)
