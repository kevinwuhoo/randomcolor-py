#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='randomcolor-py',
    version=1.0,
    description='Random color generator',
    long_description='''Generator of nice and distinct colors''',
    keywords='python random color generator',
    author='kevinwuhoo',
    author_email='me@kevinformatics.com',
    url='https://github.com/kevinwuhoo/randomcolor-py',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
    ],
)
