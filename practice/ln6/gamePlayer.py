'''
问题：
定义了玩家类Player(id, name,status,...)
人数很多，会产生大量实例
如何降低大量实例的内存开销

解决：
定义类 __slots__属性，用来声明实例属性名字的列表
'''

class Player():
	def __init__(self, uid, name, status=0, level=1):
		self.uid = uid
		self.name = name
		self.stat = status
		self.level = level

class Player2():
	# 关闭字典 提前声明实例属性 类似c结构体
	__slots__ = ['uid', 'name', 'stat', 'level']
	def __init__(self, uid, name, status=0, level=1):
		self.uid = uid
		self.name = name
		self.stat = status
		self.level = level