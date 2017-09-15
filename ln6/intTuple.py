# 如何派生内置不可变类型并修改其实例化行为
'''
问题：
定义新类型元组，传入可迭代对象，
只保留int类型且值大于0的元素

解决：
intTuple 是tuple的子类,
并实现__new__(类对象,)，修改实例化行为

'''
l = [1,-1,'abc',5,6,['x','y'],{'name':'aqie'}]

class intTuple(tuple):
	"""docstring for intTuple"""
	
	def __new__(cls,iterable):
		# 使用生成器对象
		g = (x for x in iterable if isinstance(x, int) and x > 0)
		return super(intTuple, cls).__new__(cls,g)
	def __init__(self, arg):
		print(self)
		super(intTuple, self).__init__()
		self.arg = arg

t = intTuple(l)
print(t)

'''
note: self 是tuple实例，tuple是不可变对象

'''