# 一个for语句中迭代多个可迭代对象
'''
应用：
    1.期末考试三门成绩存储在三个列表
    同时迭代三个列表，计算每个学生总分  (并行)
    2.某年级四个班，每班英语成绩存储在四个列表
    依次迭代每个列表，统计全学年成绩高于90分人数 (串行)

解决：
并行： 内置函数zip,将多个可迭代对象(合并)，每次
        迭代返回一个元组
串行： 标准库itertools.chain,可以将多个可迭代对象(连接)
'''
from random import randint

chinese = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]
english = [randint(60, 100) for _ in range(40)]

# 方法一：通过引索到三个列表取元素
# 缺点支持面窄，迭代器不支持引索
'''
for i in range(len(chinese)):
    chinese[i] + math[i] + english[i]
'''

'''
长度不一致取较短
list(zip([1,2,3,4],('a','b','c','d')))
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
'''
total = []

for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)

print(total)

#--------------华丽的分割线-------------------

from itertools import chain

english1 = [randint(60, 100) for _ in range(40)]
english2 = [randint(60, 100) for _ in range(40)]
english3 = [randint(60, 100) for _ in range(40)]
english4 = [randint(60, 100) for _ in range(40)]

print([x for x in chain(english1,english2,english3,english4) if x > 90])

count = 0
for x in chain(english1,english2,english3,english4):
    if x > 90:
        count += 1
print(count)