from os import system
from typing import List, Tuple

import re

# which is the correct way of create a type?
#Questions = NewType("Questions", List[Tuple[str, str]])
Questions = List[Tuple[str, str]]

def clear() -> int:
    """ clear the terminal using `os.system('clear')`
    """
    system('clear')
    return 0

def get_questions(
    data: str,
    beg: str,
    mid: str,
    end: str
) -> Questions: 
    """ TODO
    """
    # FIX: `end` NEED to be a non-word char like: `\$` or `\%`
    regex: str = f"{beg}([^$]*){mid}([^$]*){end}"
    question: str = ""
    answer: str = ""
    questions: Questions = []

    for question, answer in re.findall(regex, data):
        questions.append((question.strip(), answer.strip()))

    print(questions)

    return questions

def recall(questions: Questions, prefix: str, inverted: bool) -> int:
    """ TODO
    """
    question: str = ""
    answer: str = ""
    user_answer: str = ""

    for question, answer in questions:
        clear()
        print(question)
        user_answer = input(prefix)
        print("CORRECT:", answer)
        input("press [enter] for continue")

    return 0
