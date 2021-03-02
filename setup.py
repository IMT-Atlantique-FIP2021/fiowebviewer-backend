#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import (
    setup,
)

from fiowebviewer.backend.main import (
    __version__,
)


def get_install_requires():
    """
    parse requirements.txt, ignore links, exclude comments
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
          'fiowebviewer.backend',
          'fiowebviewer.backend.api',
          'fiowebviewer.backend.database',
          'fiowebviewer.backend.tools',
      ],
      install_requires=get_install_requires(),
      package_data={
          'fiowebviewer.backend': [
              'database.json',
          ],
          'fiowebviewer.backend.static': [
              'resultList.json',
          ],
      },
)
