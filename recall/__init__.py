from os import system
from typing import List, Tuple, Dict

import re

# which is the correct way of create a type?
#Questions = NewType("Questions", List[Tuple[str, str]])
Questions = List[Tuple[str, str]]

def clear() -> int:
    """ clear the terminal using `os.system('clear')`
    """
    system('clear')
    return 0

def get_questions(data: str, conf: Dict[str, str]) -> Questions: 
    """ TODO
    """
    beg: str = conf.get("regex_beg", "Q:")
    mid: str = conf.get("regex_mid", "A:")
    end: str = conf.get("regex_end", "END")
    regex: str = f"{beg}(.+?)(?={mid}){mid}(.+?)(?={end})"
    question: str = ""
    answer: str = ""
    questions: Questions = []

    for question, answer in re.findall(regex, data, re.DOTALL):
        questions.append((question.strip(), answer.strip()))

    return questions

def recall(questions: Questions, conf: Dict[str, str], inversed: bool) -> int:
    """ TODO
    """
    question: str = ""
    answer: str = ""
    user_answer: str = ""
    user_answer_prefix: str = conf.get("user_answer_prefix", "Your answer:")
    correct_answer_prefix: str = conf.get("correct_answer_prefix",
        "Correct answer:")

    for question, answer in questions:
        clear()
        print(question)
        user_answer = input(user_answer_prefix + " ")
        print(correct_answer_prefix, answer)
        input("press [enter] for continue")

    return 0
