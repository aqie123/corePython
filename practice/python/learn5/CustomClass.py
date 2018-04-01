
# 定制类

# __len__()方法我们也知道是为了能让class作用于len()函数。

class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self): 
		return 'Student object (name: %s)' % self.name
	# 偷懒写法
	__repr__ = __str__

# <CustomClass.Student object at 0x021037B0>

# 直接显示   __repr__()		: 返回程序开发者看到的字符串
# print 调用 __str__()    : 返回用户看到的字符串


# 类想被用于for ... in循环，就必须实现一个__iter__()方法
# 返回一个迭代对象,or循环就会不断调用该迭代对象的__next__()方法
# 拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

# Fib实例作用于for循环
for n in Fib():
	print(n)



# list那样按照下标取出元素，需要实现__getitem__()方法
# 对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str

class Fib(object):
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a ,b =b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L

# 先实例化
f = Fib()
print(f[0:5])



# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素。


# __getattr__()方法，动态返回一个属性
class MyStudent(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99
        elif attr == 'age':
        	return lambda:25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# s.age()


# 应用 :利用完全动态的__getattr__，我们可以写出一个链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

 Chain().status.user.timeline.list


 # 对实例本身调用 (一般 s.say()   直接调用s())
 class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


# 判断一个变量是对象还是函数
callable(Student())





