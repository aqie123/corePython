# 随机生成20个人字典
from random import randint
d = {x: randint(60,100) for x in range(1,21)}
# print(d)

# 字典解析
# Python3.5中：iteritems变为items
d = {k:v for k,v in d.items() if v >90 }
# print(d)


# 根据字典中值得大小对字典排序
a = sorted([2,4,5,2,5,6,8,34,23])
# print(a)

a = {x: randint(60, 100) for x in 'abcxyz'}
# print(a)
b = sorted(a)   # 只会按着键排序 ['a', 'b', 'c', 'x', 'y', 'z']

# 方法一： zip将字典数据转换成元组

a.keys()     # 拿到所有的键
a.values()   # 拿到所有的值
c = zip(a.values(), a.keys())
d = sorted(zip(a.values(), a.keys()))

# 方法二 : 
a = {x: randint(60, 100) for x in 'abcxyz'}
a.items() 
# dict_items([('a', 76), ('b', 97), ('c', 85), 
# ('x', 94), ('y', 76), ('z', 94)])
sorted(a.items(),key=lambda x: x[1])   # 以第一项作为比较的值


# 快速找到多个字典中的公共键
# 方法一
from random import sample
sample('abcdefg', 3)       # 生成随机进球成员

# 每个球员进球一到四个,每次三到六球员进球
# 字典解析
s1 = {x: randint(1,4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1,4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1,4) for x in sample('abcdefg', randint(3, 6))}

for k in s1:
    res = []
    if k in s2 and k in s3:
        res.append(k)


# 方法二
# 得到字典所有键集合 keys(),得到字典keys集合
# map函数，得到所有字典keys集合
# reduce取所有字典keys集合的交集
s1.keys() & s2.keys() & s3.keys()

# 扩展：统计出前n轮，每场比赛都进球人
from functools import reduce
map(dict.keys, [s1,s2,s3])
reduce(lambda a, b:a & b,map(dict.keys, [s1, s2, s3]))


