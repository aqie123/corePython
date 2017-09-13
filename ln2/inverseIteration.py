# 反向迭代 
# 需求： 实现连续浮点数发生器 FloatRange
# (start,end) step 产生连续浮点数
# FloatRange(3.0,4.0.0.2) 正反向迭代
from decimal import *
class FloatRange:
	def __init__(self, start,end,step=0.1):
		self.start = start
		self.end = end
		self.step = step
	def __iter__(self):
		tmp = self.start
		while tmp <= self.end:
			yield tmp
			tmp = round(tmp+self.step,1)
	def __reversed__(self):
		tmp = self.end
		while tmp >= self.start:
			yield tmp
			tmp = round(tmp-self.step,1)
			
for x in FloatRange(3.0,4.0,0.2):
	print(x)

for x in reversed(FloatRange(3.0,4.0,0.2)):
	print(x)
'''
反向迭代 
1. l.reverse()
2. l[::-1]
3. reversed(l)
'''