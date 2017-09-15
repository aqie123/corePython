
from lib.lib1 import Circle
from lib.lib3 import Triangle
from lib.lib2 import Rectangle

# 统一图形面积

def getArea(shape):
	for name in ('area','getArea','get_area'):
		f = getattr(shape,name,None)
		if f:
			return f()
	

shape1 = Circle(2)
shape2 = Triangle(3,4,5)
shape3 = Rectangle(6,4)

shapes = [shape1, shape2, shape3]
print(list(map(getArea, shapes)))


