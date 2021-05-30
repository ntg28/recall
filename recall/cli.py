import recall
from recall import conf

from os import (path, getenv)
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

    path_conf: str = getenv("HOME") + "/.config/recall/recall.conf"
    user_conf: Dict[str, str] = conf.conf_from(path_conf)

    fp: str = argv[1]
    questions: recall.Questions

    with open(fp, "r") as f:
        questions = recall.get_questions(f.read(), user_conf)

    if not questions:
        raise SystemExit("E: not found")

    recall.recall(questions, user_conf, False)

    return 0

def entry_point():
    try: main()
    except KeyboardInterrupt:
        print("\nClosing... Goodbye (^^)/")
