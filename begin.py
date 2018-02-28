#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: jian
@file: begin.py
@time: 2018/2/28 22:40
"""
from scrapy import cmdline

# cmdline.execute("scrapy crawl zhipin -o item.json".split())

cmdline.execute("scrapy crawl baidu".split())
