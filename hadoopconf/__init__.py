#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Read and get your Hadoop configuration as Python objects.
    For example: core-site.xml, yarn-site.xml, hdfs-site.xml
"""

from .core import get_hadoop_conf

__version__ = "1.0"

