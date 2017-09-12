# 选手解题用时记录到字典中： 字典有序
from random import randint

from collections import OrderedDict
d = OrderedDict()
# 模拟答题
from time import time

players = list('ABCDEFGH')
start = time()

for i in range(8):
	input()
	p = players.pop(randint(0, 7-i))
	end = time()
	print(i + 1, p, end -start)   # i 从零开始
	d[p] = (i+1, end-start)
print('-' * 20)
for k in d:
	print(k, d[k])

'''
range(5)      [0, 1, 2, 3, 4]
randint(a, b) a <= n <= b

'''