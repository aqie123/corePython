#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def dictsplit(func):
    def wrapper(*args, **kw):
        print('this is a decorator')
        return func(*args, **kw)
    return wrapper
