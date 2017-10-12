#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import re
from mylib.mydecorator import dictsplit

def sayhello():
    print('hello aqie')
"""
m.groups() 返回所有括号匹配的字符，以tuple格式
m.group() == m.group(0) == 所有匹配的字符
m.group(N) 返回第N组括号匹配的字符
"""

# output the first character to match
def matchone(regex_str, line):
    match_obj = re.match(regex_str, line)
    if match_obj is not None:
        # 如果group(1) reg就需要加括号
        print(match_obj.group())
    else:
        print('finds no match')

def searchone(regex_str,line):
    match_obj = re.search(regex_str, line)
    if match_obj is not None:
        print(match_obj.group())
    else:
        print('finds no match')

# 返回的是列表
def findall(regex, line, flags=0):
    match_obj = re.findall(regex, line, flags)
    if match_obj is not None:
        print(match_obj)
    else:
        print('finds none')

# 返回的是迭代器
def finditer(regex, line, flags=0):
    match_obj = re.finditer(regex, line, flags)
    if match_obj is not None:
        print([g.groups() for g in match_obj])
    else:
        print('finds none')

# 字符串替换 返回string
def sub(origin, replace, line):
    print(re.sub(origin, replace, line))

# 分割字符串 返回list
def split(separator, line):
    print(re.split(separator, line))

@dictsplit
def forL(L):
    for a in L:
        print(a)
