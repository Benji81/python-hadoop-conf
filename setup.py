#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import hadoopconf

setup(

    name='hadoopconf',

    version=hadoopconf.__version__,

    packages=find_packages(),

    author="Benjamin Quétier",

    author_email="benjamin@invenis.co",

    description="Read and get your Hadoop configuration as Python objects",

    long_description=open('README.md').read(),

    install_requires=[],

    include_package_data=True,

    url='https://github.com/Benji81/python-hadoop-conf',

    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Topic :: Communications",
    ],
)
