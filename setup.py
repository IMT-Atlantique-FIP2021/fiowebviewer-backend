#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import (
    setup,
)

from src.main import (
    __version__,
)


def get_install_requires():
    """
    Parse requirements.txt, ignore links, exclude comments

    :return: List[str]
    """
    requirements = []
    for line in open('requirements.txt').readlines():
        # skip to next iteration if comment or empty line
        if line.startswith('#') or line == '' or line.startswith('http') \
                or line.startswith('git'):
            continue
        # add line to requirements
        requirements.append(line)
    return requirements


setup(name='fiowebviewer-backend',
      version=__version__,
      description='Backend part of fiowebviewer : Webapp for visualising fio results',
      author='Sebastien Pezac',
      author_email='sebastien.pezac@imt-atlantique.net',
      packages=[
          'src',
          'src.api',
          'src.database',
          'src.models',
      ],
      install_requires=get_install_requires(),
      package_data={
          'src': [
              'database.json',
          ]
      },
      )
