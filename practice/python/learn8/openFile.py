#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open('../readfile.md','w')
  
#read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
# print(f.read())

# 'w'或者'wb'表示写文本文件或写二进制文件：
f.write("Hello Aqie")
f.close()

# with语句
with open('../readfile.md', 'r') as f:
    print(f.read())


# 如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便
'''
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
'''



# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
'''
with open('../aqie.jpg', 'rb') as f:
    print(f.read())
'''

with open('../数据结构.md', 'r', encoding='utf-8') as f:
    print(f.read())