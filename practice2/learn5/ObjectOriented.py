
# 从object继承来的
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def run():
		print('just run !')
	def print_score(self):
		print('%s : %s' % (self.name,self.score))
	def get_grade(self):
		if self.score >=90:
			return 'A'
		elif self.score >=60:
			return 'B'
		else:
			return 'C'

aqie = Student('aqie',100)
aqie.print_score()
print(aqie.get_grade())

class Dog(Student):
	pass

Dog.run()

a = Dog('aqie123','99')  # a是dog类型
# 判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(a, Dog))

# 判断继承关系
print(isinstance(a, Dog))
print(isinstance(a, Student))

# 能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance('a', str))

# 给实例绑定一个方法
def set_age(self,age):
	self.age = age

from types import MethodType
a.set_age = MethodType(set_age, a)

a.set_age(25)
print(a.age)

# 所有实例都绑定方法，可以给class绑定方法：

def set_score(self,score):
	self.score = score

Student.set_score = set_score

a.set_score(100)
a.print_score()

# __slots__变量，来限制该class实例能添加的属性
class Animal(object):
    __slots__ = ('name', 'age','score') # 用tuple定义允许绑定的属性名称
    def get_score(self):
    	return self._score
    def set_score(self, value):
    	if not isinstance(value, int):
    		raise ValueError('score must be an integer!')
    	if value < 0 or value > 100:
    		raise ValueError('score must between 0 ~ 100!')
    	self._score = value