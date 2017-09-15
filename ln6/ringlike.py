

# 引用计数
class A(object):
	def __del__(self):
		print('in __del__')


# 创建实例
a = A()

import sys

# 查看连接数   2-1比想要的多一个
print(sys.getrefcount(a))  
a2 = a

print(sys.getrefcount(a))  # 3

del a2

print(sys.getrefcount(a))

a = 5

print(sys.getrefcount(a))


print('------------------')
b = A()
print(sys.getrefcount(b)-1) 

import weakref

# 创建对象弱引用
b_wref = weakref.ref(b)

b2 = b_wref()

print(b2 is b)

print(sys.getrefcount(b) - 1)

del b
del b2

print(b_wref() is None)