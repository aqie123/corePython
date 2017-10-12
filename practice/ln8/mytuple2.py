
from functools import update_wrapper, wraps,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES
def mydecorator(func):
	def wrapper(*arg, **kargs):
		''' wrapper function'''
		print('in wrapper')
		func(*args, **kargs)
	# wrapper.__name__ = func.__name__   不优雅
	# update_wrapper(wrapper,func,('__name__','__doc__'),('__dict__',))
	update_wrapper(wrapper,func)  # 使用默认参数
	return wrapper

@mydecorator
def example():
	'''example function'''
	print('in example')

print(example.__name__)  # example (保留元数据)

print(example.__doc__)   #  wrapper function

#-----------------------------
'''
标准库 functools中装饰器 wraps装饰内部包裹函数
可制定原函数某些属性，更新到包裹函数上面
'''

print(WRAPPER_ASSIGNMENTS)  
# ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')


print(WRAPPER_UPDATES)
# ('__dict__',)
