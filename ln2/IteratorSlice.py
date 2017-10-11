# 对迭代器做切片操作
# 问题; python中文本文件是可迭代对象
f = open('slice.txt')
# f[5:10]  报错
lines = f.readlines()   #指针跑到文件结尾处
# lines[5:10]   可以,缺点一次性读入
'''
f.seek(0)
for line in f:
	print(line)
'''

# 标准库itertools.islice ,返回迭代对象切片生成器
from itertools import islice
myfile = open('slice.txt')

for line in islice(myfile,5,10):
	print(line)