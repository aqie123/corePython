from lib.lib1 import Circle
from lib.lib3 import Triangle
from lib.lib2 import Rectangle

from operator import methodcaller

s = 'abc123abc456'
a = s.find('abc',4)

print(a)  # 6

b = methodcaller('find','abc',4)(s)
print(b)