
import weakref
class Data(object):
	"""docstring for Data"""
	def __init__(self, value, owner):
		self.value = value
		# 变为弱引用
		self.owner = weakref.ref(owner)

	def __str__(self):
		# 变为函数调用 owner()
		return "%s's data,value is %s" % (self.owner(), self.value)
	
	def __del__(self):
		print('in Data.__del__')	

class Node(object):
	"""docstring for ClassName"""
	def __init__(self, value):
		self.data = Data(value, self)

	def __del__(self):
		print('in Node__del__')


node = Node(100)
del node
input('wait...')
	
'''
垃圾回收
import gc
gc.collect()
'''
