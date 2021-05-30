from setuptools import (setup, find_packages)

name: str = "recall"
desc: str = "Python scripts for Active Recall learning method"
version: str = "0.1"
entry_points: dict = {
    "console_scripts": [
        "recall=recall.cli:entry_point"
        ]
    }

setup(
    name=name,
    description=desc,
    version=version,
    packages=find_packages(),
    entry_points=entry_points
    )
