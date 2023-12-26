from state_capitals import capitals
from pathlib import Path
from random import choice
from os import walk
from icecream import ic as pyprint

# 1. What is the capital of blah blah?
# a. b. c. d.


def create_quiz():
    """Generates docs for sets of questions"""

    for number in range(3):
        path = Path(f"random_questions/question_files/set-{number}.docx")
        if path.exists():
            return
        path.touch()


def create_question():
    """Generates"""

    choice_list = ["a", "b", "c", "d"]

    for folder_names, subfolder_names, file_names in walk(
        Path("random_questions/question_files/")
    ):
        for key, value in capitals.items():
            selected_answer = choice(choice_list)
            file_path = Path(f"random_questions/question_files/set-{number}.docx")
            with open(file_path, "w", encoding="UTF-8") as file_object:
                file_object.write(f"{number}. What is the capital of {key}?\n")
                for answer_choice in choice_list:
                    file_object.write(
                        f"{answer_choice}. {value if selected_answer==answer_choice else choice(list(capitals.values()))}"
                    )


# for key, value in capitals.items():
#         selected_answer = choice(choice_list)
#         file_path = Path(f"random_questions/question_files/set-{number}.docx")
#         with open(file_path, "w", encoding="UTF-8") as file_object:
#             file_object.write(f"{number}. What is the capital of {key}?\n")
#             for answer_choice in choice_list:
#                 file_object.write(
#                     f"{answer_choice}. {value if selected_answer==answer_choice else choice(list(capitals.values()))}"
#                 )


for foldername, subfoldername, filenames in walk(
    Path("random_questions/question_files/")
):
    for name in filenames:
        pyprint(name)
