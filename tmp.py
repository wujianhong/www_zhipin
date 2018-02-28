#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: jian
@file: tmp.py
@time: 2018/2/28 23:55
"""


class Abc(object):
    def __init__(self):
        self.index = 0

    def start_requests(self):
        return [self.next_request()]

    def asd(self):
        self.index += 1
        print("parse1", self.index)
        yield self.next_request()

    def next_request(self):
        print("next_request", self.index)
        return self.asd()


if __name__ == '__main__':
    a = Abc()
    b = a.start_requests()
    # b = a.asd()
    for tmp in b:
        for o in tmp:
            print(o)
