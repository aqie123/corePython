# -*- coding: utf-8 -*-
print('啊切')

# 计算一百以内所有奇数之和
sum = 0;
n = 99;
while n > 0:
  sum = sum + n 
  n = n-2

print(sum)

sum  = 0
for x in range(101):
  sum = sum + x
print(sum)


# 循环和占位符 (两种写法)
L = ['Bart', 'Lisa', 'Adam']
for x in L:
  print("hello: %s" % x)
  print('hello,'+x+'!')

# 字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Bob']
d.get('Thomas', -1)
d.pop('Bob')  # 删除
