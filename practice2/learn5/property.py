
# @property装饰器就是负责把一个方法变成属性调用的
class Student(object):

    @property
    def score(self):
        return self._score

	# @property本身又创建了另一个装饰器@score.setter
	# 负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 88  # 实际转化为s.set_score(60)
print(s.score)

# property给一个Screen对象加上width和height属性，以及一个只读属性resolution
# 只定义getter方法，不定义setter方法就是一个只读属性
class Screen(object):
	@property
	def width(self):
		return self._width
	@property
	def height(self):
		return self._height
	# 只读属性
	@property
	def resolution(self):
		return self._width * self._height

	@width.setter
	def width(self,value):
		self._width = value

	@height.setter
	def height(self,value):
		self._height = value