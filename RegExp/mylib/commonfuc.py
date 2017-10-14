#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import time

def timestamp():
    print(time.time())

def mytime():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

def foo(*args, **kwargs):
    print 'args = ', args
    print 'kwargs = ', kwargs
