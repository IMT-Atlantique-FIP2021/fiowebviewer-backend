#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import (
    setup,
)

from backend.main import (
    __version__,
)


def get_install_requires():
    """
    Parse requirements.txt, ignore links, exclude comments

    :return: List[str]
    """
    requirements = []
    with open("requirements.txt") as f_requirements:
        for line in f_requirements.readlines():
            # skip to next iteration if comment or empty line
            if (
                line.startswith("#")
                or line == ""
                or line.startswith("http")
                or line.startswith("git")
            ):
                continue
            # add line to requirements
            requirements.append(line)
    return requirements


setup(
    name="fiowebviewer-backend",
    version=__version__,
    description="Backend part of fiowebviewer : Webapp for visualising fio results",
    author="Sebastien Pezac",
    author_email="sebastien.pezac@imt-atlantique.net",
    packages=[
        "backend",
        "backend.api",
        "backend.database",
        "backend.models",
    ],
    install_requires=get_install_requires(),
    package_data={
        "backend": [
            "database.json",
        ]
    },
)
