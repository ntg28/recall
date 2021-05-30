import re
from os import path
from typing import Dict

def conf_from(fp: str) -> Dict[str, str]:
    if not path.exists(fp):
        return {}

    key: str = ""
    val: str = ""
    conf: Dict[str, str] = {}
    regex: str = "^(\w+)\s*=\s*(.*)$"

    with open(fp, "r") as f:
        for key, val in re.findall(regex, f.read(), re.MULTILINE):
            conf[key] = val.strip()

    return conf
