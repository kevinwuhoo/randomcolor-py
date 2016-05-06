#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os

setup(
    name='randomcolor',
    version='0.4.4.1',
    description='For generating attractive random colors',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    keywords='python random color generator',
    author='Kevin Wu',
    author_email='me@kevinformatics.com',
    url='https://github.com/kevinwuhoo/randomcolor-py',
    packages=['randomcolor'],
    include_package_data=True,
    install_requires=[],
)
