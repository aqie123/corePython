class Rectangle(object):
	"""docstring for Rectangle"""
	def __init__(self, w,h):
		self.w = w
		self.h = h
	def get_area(self):
		return self.h * self.w