
class Attr(object):
	def __init__(self,name,type_):
		self.name = name
		self.type_ = type_

	def __get__(self, instance, cls):
		# print('in __get__',instance,cls)
		return instance.__dict__[self.name]

	def __set__(self, instance, value):
		if not isinstance(value,self.type_):
			raise TypeError('expected an %s' % self.type_)
		instance.__dict__[self.name] = value

	def __delete__(self,instance):
		del isinstance.__dict__[self.name]

class Person(object):
	# 类属性是描述符实例
	name = Attr('name',str)
	age = Attr('age',int)
	height = Attr('height',float)

p = Person()
p.name = 'aqie'
p.age = '123'