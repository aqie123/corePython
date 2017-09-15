from gamePlayer import Player, Player2

p1 = Player('0001','Jim')

p2 = Player2('0002','Jim')

# 查看对象
dir(p1)

# 将p1,p2做成集合
set(dir(p1)) - set(dir(p2))   # {'__weakref__', '__dict__'}

p1.__dict__
# 为p1动态绑定属性的字典 eg: p1.x
# {'uid': '0001', 'name': 'Jim', 'stat': 0, 'level': 1}

# 直接赋属性
p1.__dict__['y'] = 99

# 删除属性
del p1.__dict__['y']

#----------华丽的分割线---------
import sys
sys.getsizeof(p1.__dict__)   # 字典占据204 字节


# 会报错
p2.x = 1