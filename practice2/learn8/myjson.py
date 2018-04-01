
'''
json   : {}, [], "string" , 123.45, true/false, null

python : dict,list,str, int/float,True/False,Null

'''

import json
d =  dict(name='Bob', age=20, score=88)
# 把Python对象变成一个JSON：
d = json.dumps(d)
print(d)


# dump()方法可以直接把JSON写入一个file-like Object

# json进阶
# 1.dict对象可以直接序列化为JSON的{}
# 2. class类转换为json



def student2dict(std):
  return {
    'name': std.name,
    'age': std.age,
    'score': std.score
  }

class Student(object):
  def __init__(self, name, age, score):
    self.name = name
    self.age = age
    self.score = score

s = Student('aqie', 16, 99)
print(json.dumps(s,default=student2dict))

# 任意class的实例变为dict
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量


class Teacher(object):
  def __init__(self, name, age, score):
    self.name = name
    self.age = age
    self.score = score
s = Teacher('aqie123', 16, 98)
print(json.dumps(s, default=lambda obj: obj.__dict__))


# 定义了__slots__的class。

# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
# loads()方法首先转换出一个dict对象
# 我们传入的object_hook函数负责把dict转换为Student实例

# 反序列化

def dict2student(d):
  return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))


# 总结
# Python语言特定的序列化模块是pickle，json模块更通用、更符合Web标准