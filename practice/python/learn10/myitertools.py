import itertools

# 无限迭代器
'''
natuals = itertools.count(1)
for n in natuals:
	print(n)
'''

# cycle()会把传入的一个序列无限重复下去
'''
items  = itertools.cycle('aqie')
for i in items:
	print(i)
'''


# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
items = itertools.repeat('aqie',2)
for n in items:
	print(n)


# 截取无限序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x : x <= 10, natuals)
print(list(ns))


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('abc','def'):
	print(c)

# groupby()把迭代器中 相邻 的重复元素挑出来放在一起
for key, group in itertools.groupby('jaAAAAACCCNKAMVPPJAnvncasjm,vmssak', lambda c: c.upper()):
	print(key, list(group))