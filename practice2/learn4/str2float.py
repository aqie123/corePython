# -*- coding: utf-8 -*-

from functools import reduce

def fn(x, y):
  return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
  '6': 6, '7': 7, '8': 8, '9': 9}[s]

# '123.456'
# if str.isdigit(): 判断是否是数字
string = '123.4567'

a= string.index('.')
b = len(string)

# 转换成list
def str2list(s):
	A = []
	for x in s:
		if x.isdigit():
			A.append(x)
	return A

B = str2list(string)
# list 转换为数字
C = list(map(int, B))

# [1, 2, 3, 4, 5, 6] 

# 获取到小数点位数
D = reduce(fn, C)
print(D)
print(a)
print(b)
c = b-a-1

# 根据位数处理被除数
def  divisor(n):
	s = 1
	while n>0:
		n = n-1
		s = 10 * s
	return s

final = D/divisor(c)
print(final)