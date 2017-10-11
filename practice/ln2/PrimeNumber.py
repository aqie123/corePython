# 实现可迭代对象的类，迭代出给定范围所有素数
# 迭代器对象  生成器对象
# 解决方法：将该类的__iter__方法实现生成器函数,每次yield返回一个素数


# 生成器对象: (实现了可迭代接口，也实现了迭代器接口)

class PrimeNumbers(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end
	def isPrimeNum(self, k):
		if k < 2:
			return False
		for i in range(2, k):
			if k % i == 0:
				return False
		return True
	def __iter__(self):
		for k in range(self.start, self.end + 1):
			if self.isPrimeNum(k):
				yield k

# 创建1到100对象
for x in PrimeNumbers(1,100):
	print(x)