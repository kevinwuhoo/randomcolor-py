#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

setup(
    name='randomcolor',
    version='0.4.4.0',
    description='For generating attractive random colors',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')),
    keywords='python random color generator',
    author='Kevin Wu',
    author_email='me@kevinformatics.com',
    url='https://github.com/kevinwuhoo/randomcolor-py',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)
