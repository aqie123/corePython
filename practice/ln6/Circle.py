
from math import pi

class Circle(object):
	def __init__(self, radius):
		self.radius = radius

	def getRadius(self):
		return round(self.radius, 2)

	def setRadius(self,value):
		if not isinstance(value,(int, float)):
			raise ValueError(' wrong type')
		self.radius = float(value)

	def getArea(self):
		return self.radius ** 2 * pi
	R = property(getRadius,setRadius)

c = Circle(3.2)

# 调用属性 程序赋值错误，但运行不会出错
'''
c.radius = 'abc'
d = c.radius * 2
print(d)
'''
# 调用函数会抛出异常
c.setRadius(8.345)
r = c.getRadius()
print(r)

# 修改后
c.R = 3.1415926

print(c.R)