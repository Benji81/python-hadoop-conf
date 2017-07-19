# python-hadoop-conf
Read your Hadoop configuration files and get a dictionary of properties.

Usage:
```python
    from hadoopconf import get_hadoop_conf
    conf = get_hadoop_conf()
    print(conf['yarn.resourcemanager.webapp.address'])
```

