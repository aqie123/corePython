# list 详解
from random import randint
import timeit 

# -10 到10 随机生成十个
# range()与xrange()合并为range( )
data = [randint(-10, 10) for _ in range(10)]

# 方法一： filter
'''
data = filter(lambda x: x >= 0, data)
print(list(data))
'''


# 方法二：列表解析 (更快)
'''
data = [randint(-10, 10) for _ in range(10)]
data = [x for x in data if x >= 0]
print(data)
'''

# note  timeit filter(lambda x: x >= 0, data)  测试程序运行时间


'''
统计序列中的元素出现个数
'''
data = [randint(0,20) for _ in range(30)]
print(data)

c = dict.fromkeys(data, 0)  # 以data值为键，0为值
for x in data:
  c[x] += 1
print(c)

'''
找到频度出现次数最高三个元素
'''

# 根据列表中的值进行排序
'''
def sortedDictValues1(adict):
    keys = adict.keys()
    sorted(keys)
    return map(adict.get,keys)
print(list(sortedDictValues1(c)))
'''
# Python3.5中：iteritems变为items
# 方法一：
'''
dict= sorted(c.items(), key=lambda d:d[1], reverse = True)
print(dict)

print(dict[:3])
'''

# 方法二 
# 序列传入Counter的构造器，得到Counter对象是元素频度的字典
# Counter.most_common(n) 得到频度最高的n个元素的列表
from collections import Counter
c2 = Counter(data)    # 和上面c一样
c2.most_common(3)