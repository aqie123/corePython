from random import randint
# 集合解析
data = [randint(-10, 10) for _ in range(10)]

# list 转换为set
s = set(data)
print(s)

# 找到能被三整除的子集合
s = {x for x in s if x % 3 == 0}
print(s)