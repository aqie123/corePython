# 为被装饰函数保存元数据
'''
问题：
函数对象保存函数元数据
f.__name__ : 函数的名字
f.__doc__  : 函数文档字符串
f.__module__ : 函数所属模块名
f.__dict__   : 属性字典
f.__deault__ : 默认参数元组

使用装饰器后，上面属性访问的是内部包裹函数的
元数据，原来函数的元数据丢失掉

解决： 

'''

def f(a):
	"""f function aqie """
	def __init__(self,name):
		self.name = name
	return a * a

f.__name__

g = f
g.__name__

f.__doc__

f.__module__  # '__main__'

#----------------------------

def fn(a,b = 1, c = []):
	print(a, b, c)

fn.__defaults__[1].append('abc')

fn(100)    # 100 1 ['abc']   默认参数不要使用可变对象

#----------闭包---------

def fuc():
	a = 2
	return lambda k: a ** k

g = fuc()
c = g.__closure__[0]

c.cell_contents    # 访问 2