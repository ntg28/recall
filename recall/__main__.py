import __init__ as recall

from os import path
from sys import argv

def main(fp: str) -> int:
    """ TODO
    """
    if not path.exists(fp):
        raise SystemExit("file not exists")

    fdata: str = ""
    question: str = ""
    answer: str = ""
    questions: Questions

    with open(fp, "r") as f:
        fdata = f.read()

    questions = recall.get_questions(fdata,
        beg="Q:", mid="A:", end="\$")

    recall.recall(questions, prefix="YOUR ANSWER: ", inverted=False)

    return 0

if __name__ == "__main__":
    argc: int = len(argv)
    if argc < 2:
        raise SystemExit("missing argument, use: recall [FILE]")

    main(argv[1])
