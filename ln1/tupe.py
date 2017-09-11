
student = ('aqie', 16, 'male', '2924811900@qq.com')
print(student[0])

# 方法一使索引易读 定义数值常量
# NAME = 0
# AGE = 1
# SEX = 2 
# EMAIL = 3

NAME, AGE, SEX, EMAIL = range(4)

print(student[EMAIL])

# 方法二使用标准库中 collections.namedtuple 替代内置tuple

from collections import namedtuple
Student = namedtuple('Student',['name', 'age', 'sex', 'email'])
s = Student('aqie', 16, 'male', '2924811900@qq.com')
print(s)
print(s.name)

print(isinstance(s, tuple))  # 内置元组子类