
import random
'''
斐波那契数列 Fibonacci Sequence 黄金分割数列
1,1,2,3,5,8,13
'''
def Fibonacci(n, cache = None):
	if cache is None:
		cache = {}
	if n in cache:
		return cache[n]
	if n <= 1:
		return 1
	cache[n] = Fibonacci(n-1,cache) + Fibonacci(n-2,cache)
	return cache[n]

print(Fibonacci(50))

'''
十个台阶,每次1-3，不能后退，有几种走法

分析：仅剩最后一步要走
1.只需要走一步 f(n-1)种走法
2.需要走两步,f(n-2)种走法
3.需要走三步,f(n-3)种走法
f(n) = f(n-1) + f(n-2) + f(n-3)

'''
def ladder(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	if n == 3:
		return 4
	return ladder(n-1) + ladder(n-2) + ladder(n-3)

print(ladder(10))


def climb(n,steps):
	count = 0
	if n == 0:
		count =1
	elif n > 0:
		for step in steps:
			count += climb(n-step,steps)
	return count

lists = list(range(1,4))

print(climb(10,lists))



'''
n个台阶，每次走1-m阶，不能后退，有几种走法
'''



