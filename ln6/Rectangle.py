
# 比较矩形实例
# < <=,>,>=,==,!=
# __lt__,__le__,__gt__,__ge__,__eq__,__ne__
'''
class Rectangle(object):
	def __init__(self, w,h):
		self.w = w
		self.h = h
	def area(self):
		return self.w * self.h

	# 实现实例比较
	def __lt__(self,obj):
		return self.area() < obj.area()
	def __gt__(self,obj):
		return self.area() > obj.area()

r1 = Rectangle(3,4)
r2 = Rectangle(1,2)

print(r1 < r2) # r1.__lt__
'''

#-------------------华丽的分割线-------------
'''
定义抽象基类
'''

from functools import total_ordering
from abc import ABCMeta, abstractmethod

@total_ordering
class Shape(object):
	# 实现实例比较
	def __lt__(self,obj):
		if not isinstance(obj, Shape):
			raise TypeError('obj is not Shape')
		return self.area() < obj.area()
	def __eq__(self,obj):
		if not isinstance(obj, Shape):
			raise TypeError('obj is not Shape')
		return self.area() == obj.area()
	# 描述抽象接口,子类必须实现
	@abstractmethod
	def area(self):
		pass



class Rectangle(Shape):
	"""docstring for Rectangle"""
	def __init__(self, w,h):
		self.w = w
		self.h = h
	def area(self):
		return self.w * self.h

	

class Circle(Shape):
	def __init__(self,r):
		self.r = r
	def area(self):
		return self.r ** 2 * 3.14


# 实现area接口就可以进行比较
r1 = Rectangle(3,4)
r2 = Rectangle(1,2)
c1 = Circle(3)

print(r1 >= r2)
print(r1 <= c1)
print(c1 <= 3)
