print(type(123))
class MyObject(object):
  def __init__(self):
    self.x = 9
  def power(self):
    return self.x * self.x

obj = MyObject()

hasattr(obj,'x')

setattr(obj, 'y', 19)

getattr(obj, 'y') 

obj.y          # 19

hasattr(obj, 'power')   # True

fn = getattr(obj, 'power')

# 实例绑定属性属性两种方法
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 类本身绑定属性 （实例属性优先级比类属性高）
class Student(object):
    name = 'Student'