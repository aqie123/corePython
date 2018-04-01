def my_max(a, b):
	z = [False for i in (a,b) if not isinstance(i, (int, float))]
	if z:
		raise TypeError('bad operand type')
	if a > b:
		return a
	else:
		return b

def say_hello():
	print("hello啊切")

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 定义求任何数任何次方

def power(x, n = 2):
	s = 1
	while n > 0:
		n = n-1
		s = x * s
	return s

# a2 + b2 + c2 + ……
def calc(*numbers):
	sum = 0
	for x in numbers:
		sum = sum + x * x
	return sum 
# 递归
def cursion(n):
	if n==1:
		return 1	
	return  n * cursion(n-1)

# 尾递归
def fact(n):
	return (n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# 汉诺塔
def Hanoi_iter(n, number):
	if n == 1:
		return number
	return Hanoi_iter(n-1, 1+2*number)
