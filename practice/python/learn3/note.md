1.iteration (迭代)
	a.Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上
	b.dict迭代的是key。如果要迭代value，可以用for value in d.values()
		for k, v in d.items()
	c.判断是否可以迭代
		1.from collections import Iterable
		2.isinstance('abc', Iterable)
	d. for x, y in [(1, 1), (2, 4), (3, 9)]:
 		内置的enumerate函数可以把一个list变成索引-元素对
2.列表生成式即List Comprehensions
	a.list(range(1, 11))
	b. [x * x for x in range(1, 11)]             前面要生成数
	c.[x * x for x in range(1, 11) if x % 2 == 0] 后面可以加判断条件
	d.列出当前目录下的所有文件和目录名，可以通过一行代码实现
		1.import os 
		2.[d for d in os.listdir('.')]
	f. [k + '=' + v for k, v in d.items()]      列表生成式用两个变量
	g. isinstance(x, str) 判断一个变量是不是字符串
3.一边循环一边计算的机制，称为生成器：generator
	a.创建生成器
		1.只要把一个列表生成式的[]改成()
		2.yield关键字
			利用 for in 循环 输出generator函数
		3. for 循环拿到返回值 
			(捕获StopIteration错误，返回值包含在StopIteration的value中)


	b. for in 遍历 生成器


	c.斐波拉契数列(Fibonacci )

	d.杨辉三角 Pascal's Triangle
		(每个数等于上方两个数之和)： generator，不断输出下一行的list
		1. 每一行看成一个list

4.生成器：generator
	1. 只要把一个列表生成式的[]改成()，就创建了一个generator
		L = [x * x for x in range(10)]
		g = (x * x for x in range(10))
	2.如果一个函数定义中包含yield关键字，
	  那么这个函数就不再是一个普通函数，而是一个generator
5.迭代器 
	1.（for循环的对象统称为可迭代对象：Iterable）: 生成器都是Iterator对象
	2. 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator(表示的数据流)
		list、dict、str虽然是Iterable，却不是Iterator
	可以直接作用于for循环的数据类型有以下几种：

	一类是集合数据类型，如list、tuple、dict、set、str等；

	一类是generator，包括生成器和带yield的generator function。
	a.isinstance()判断一个对象是否是Iterable对象
	b. from collections import Iterable
	c.isinstance([], Iterable)
