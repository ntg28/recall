import recall

from os import path
from sys import argv
from typing import (Dict, List)

def argv_validation(argv: List[str]) -> int:
    """ TODO
    """
    argc: int = len(argv)
    if argc < 2:
        return 1
    if not path.exists(argv[1]):
        return 2
    return 0

def main() -> int:
    argv_err: int = argv_validation(argv)

    if (argv_err == 1):
        raise SystemExit("E: missing [FILE] parameter.")

    elif (argv_err == 2):
        raise SystemExit(f"E: {argv[1]} not exists.")

    fp: str = argv[1]
    prefix: str = "Your Answer: "
    question: recall.Questions

    with open(fp, "r") as f:
        questions = recall.get_questions(f.read(),
            beg="Q:", mid="A:", end="END")

    recall.recall(questions, prefix=prefix, inverted=False)

    return 0

def entry_point():
    try: main()
    except KeyboardInterrupt:
        print("\nClosing... Goodbye (^^)/")
