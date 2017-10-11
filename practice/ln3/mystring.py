# 拆分含有多种分隔符的字符串
# , ; | \t 都是分隔符  split
s = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
# 方法一： 多次处理
# a= map(lambda x: x.split('|'),a)   # 变成二维数组


def mySplice(s, ds):
	res = [s]
	for d in ds:
		t = []
		list(map(lambda x: t.extend(x.split(d)),res))
		res = t
	return [x for x in res if x]    # 过滤空字符串
print(mySplice(s,';,|\t'))