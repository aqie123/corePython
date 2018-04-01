# 元类

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

# h = Hello()   h.hello()
# type()函数可以查看一个类型或变量的类型
# Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello


# 通过type()函数创建出Hello类
	
# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

def fn(self, name='world'): # 先定义函数
	print("Hello, %s" % name)

Hello = type('Hello',(object,), dict(hello=fn))  # tuple的单元素写法


# 先定义metaclass，就可以创建类，最后创建实例

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
class MyList(list, metaclass = ListMetaclass):
	pass

