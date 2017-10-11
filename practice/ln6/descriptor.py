
class Descriptor(object):
	def __get__(self, instance, cls):
		print('in __get__',instance,cls)
		return instance.__dict__['x']

	def __set__(self, instance, value):
		print('in __set__',instance,value)
		# x变成a的属性
		instance.__dict__['x'] = value

	def __delete__(self,instance):
		print('in __del__')

class A(object):
	# 类属性是描述符实例
	x = Descriptor()

a = A()

# 对a 赋值会被描述符截获

# x变为a属性后这里报错
# a.x
# in __get__ <__main__.A object at 0x00613190> <class '__main__.A'>

# A.x # in __get__ None <class '__main__.A'>

a.x = 3

print(a.__dict__)   # {}  x 不是a 的属性
print(a.x)