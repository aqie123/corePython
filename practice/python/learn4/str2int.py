
from functools import reduce
def char2num(s):
  return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
  '6': 6, '7': 7, '8': 8, '9': 9}[s]

def fn(x, y):
  return x * 10 + y

a = reduce(fn,list(map(char2num,"123")))
print(a)

# 合二为一
def str2int(s):
  def fn(x, y):
    return x * 10 + y
  def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
  '6': 6, '7': 7, '8': 8, '9': 9}[s]
  return reduce(fn,list(map(char2num,s)))

# lambda函数进一步简化成
def str2int(s):
  return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# name = ['adam', 'LISA', 'barT']
def normalize(name):
  return list(map(lambda x: x.capitalize(), name))

def prod(L):
  return reduce(lambda x ,y: x*y,L)