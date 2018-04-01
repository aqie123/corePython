from collections import namedtuple
# namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
Point = namedtuple('Point',['x','y'])

p = Point(1, 2)
print(p.x)

isinstance(p, Point)
isinstance(p, tuple)

# list 按索引访问元素很快,删除插入元素很慢
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈

from collections import deque 
q = deque(['a','q','i','e'])
q.append(123)
q.appendleft('k')
print(q)

# dict中key是无序的,dict做迭代无法确定key顺序
# OrderedDict 保持key的顺序
from collections import OrderedDict
d = dict([('a', 1), ('e', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('e', 2), ('c', 3)])
print(od)

# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3

print(list(od.keys()))

# deque 实现list  append()  pop() appendleft()  popleft()

# Counter 计数器  统计字符出现个数
from collections import Counter
c = Counter()
for ch in 'programming'
	c[ch] = c[ch] + 1