
import random

def memo(func):
	cache = {}
	# 收集参数
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return wrap



'''
斐波那契数列 Fibonacci Sequence 黄金分割数列
1,1,2,3,5,8,13
'''
@memo
def Fibonacci(n):
	if n <= 2:
		return 1
	return Fibonacci(n-1) + Fibonacci(n-2)

# Fibonacci = memo(Fibonacci)
print(Fibonacci(5))


'''
n个台阶，每次走1-m阶，不能后退，有几种走法
'''
@memo
def climb(n,steps):
	count = 0
	if n == 0:
		count =1
	elif n > 0:
		for step in steps:
			count += climb(n-step,steps)
	return count

lists = tuple(range(1,100))

print(climb(101,lists))







