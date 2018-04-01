L = list(range(1,4))
def f(x):
  return x

M = map(f,L)
# print(M)     # 这是个map 对象; 结果M是一个Iterator，Iterator是惰性序列
print(list(M)) # [1, 2, 3]
def add(x,y):
  return x + y

from functools import reduce

print(reduce(add, L))  # 0+...+9 1+2+3 = 6

def f(x,y):
  return x * y

print(reduce(f,L))