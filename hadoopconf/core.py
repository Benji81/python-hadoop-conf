#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Implementation

    Usage:

    >>> from hadoopconf import get_hadoop_conf
    >>> get_hadoop_conf()
"""


#  String list of what we can import from the lib
import os
import re
import xml.etree.ElementTree as Et

__all__ = ['get_hadoop_conf']


class NoHadoopConfDir(Exception):
    pass


def get_conf_dir(dirname=None):
    """
    Return the Hadoop configuration directory absolute path. Raise a NoHadoopConfDir exception if
    no environment variable defined it (HADOOP_CONF_DIR or HADOOP_HOME) or if dirname is not a valid directory path
    :param dirname: Optional absolute path of a directory that should contains *-site.xml files
    :return:
    """
    if dirname:
        if os.path.exists(dirname) and os.path.isdir(dirname):
            return dirname
        else:
            NoHadoopConfDir()
    if 'HADOOP_CONF_DIR' in os.environ:
        return os.environ['HADOOP_CONF_DIR']
    if 'HADOOP_HOME' in os.environ:
        dirname = os.path.join(os.environ['HADOOP_HOME'], 'etc', 'hadoop')
        if os.path.exists(dirname) and os.path.isdir(dirname):
            return dirname
        else:
            NoHadoopConfDir()
    else:
        raise NoHadoopConfDir()


def get_conf_files(dirname):
    """
    Generator of all *-site.xml files in a directory
    :param dirname: absolute path of a directory that should contains *-site.xml files
    :return:
    """
    for file in os.listdir(dirname):
        if re.match(r'.+-site\.xml', file):
            yield os.path.join(dirname, file)


def parse_file(file):
    """
    Parse an xml Hadoop property file
    :param file: absolute path
    :return: a dictionary (propertyName -> propertyValueInString)
    """
    tree = Et.parse(file)
    root = tree.getroot()
    result = dict()
    for child in root.findall('property'):  # Find all properties names an values
        result[child.find('name').text] = child.find('value').text
    return result


def get_hadoop_conf(dirname=None):
    """
    Return a dict of all properties find in all *-site.xml files on your Hadoop configuration directory.
    It will search in your env variable HADOOP_CONF_DIR next in HADOOP_HOME/etc/hadoop or in dirname if you specify it
    :param dirname: optional directory absolute path that contains *-site.xml file
    :return: a dictionary (propertyName -> propertyValueInString)
    """
    dirname = get_conf_dir(dirname)
    files = get_conf_files(dirname)
    all_conf = dict()
    for file in files:
        all_conf.update(parse_file(file))  # Merge dictionnaries
    return all_conf


if __name__ == '__main__':
    conf = get_hadoop_conf()
    print(conf['yarn.resourcemanager.webapp.address'])
