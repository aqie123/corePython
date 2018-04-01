# 多重继承
class Animal(object):
	pass

# 大类
class Mammal(Animal):
	pass

class Bird(Animal):
	pass


# 各种动物
class Dog(Mammal, RunnableMixIn):
	pass

class Bat(Mammal, FlyableMixIn):
	pass

class Parrot(Bird, FlyableMixIn):
	pass
class Ostrich(Bird, RunnableMixIn):
	pass

# 细分类
class RunnableMixIn(object):
	def run(self):
		print("Running")

class FlyableMixIn(object):
	def fly(self):
		print("Fying")

class CarnivorousMixIn(object):
	def eatGress(self):
		print("食肉动物")

class HerbivoresMixIn(object):
	def eatMeat(self):
		print("食草动物")



# 应用
# 多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

# 多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass