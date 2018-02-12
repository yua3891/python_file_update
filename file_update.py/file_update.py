#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#@Author: ken
#@Time:2018/2/1 0001 下午 17:42
#@File:test.py

import os
import time

br = True
path = os.getcwd() + '/www.test.cc/index.html'
time_old = 0
time_last = 0
mod = True

def jianceDir():
    try:
        _time_last = os.path.getmtime(path)
        return _time_last
    except:
        print('文件不存在')
        exit(0)

def readFile():
    _f = open(path)
    _content = _f.read()
    print(_content)
    _f.close()

if __name__ == '__main__':
    while(True):
        time_last = jianceDir()
        if (time_old != time_last):
            time_old = time_last
            readFile()
        print('listing...')
        time.sleep(0.5)
