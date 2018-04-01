1.高阶函数英文叫Higher-order function
	a。函数本身也可以赋值给变量，即：变量可以指向函数
	b.函数名其实就是指向函数的变量
  c.函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
2.map 
  a。 map()函数接收两个参数，一个是函数，一个是Iterable，
      map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
  b. list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
3.reduce 
  a。这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
     reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
  b。 [1, 3, 5, 7, 9]变换成整数13579
    1. L=list(range(1,10))   f = 10*x +y
    2. reduce(f,L[::2])

    另一种： int(reduce(f,list(map(str,L[::2]))))  f = x + y

4. 
  a。练习 str 转换int
  b. ['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
      1. "ADC".lower()
      2.upper() 全部大写
      3. capitalize() 首字母大写其余全部小写
      4.title()   标题首字母大写
  c. 把字符串'123.456'转换成浮点数123.456


5. filter
  a.把传入的函数依次作用于每个元素,然后根据返回值是True还是False决定保留还是丢弃该元素
  	保留返回true的
  b. filter()函数返回的是一个Iterator，也就是一个惰性序列
  c.filter()的作用是从一个序列中筛出符合条件的元素。
  	由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素


6. 练习
	1. 用filter求素数
	2. filter 求回数

7.sorted 排序
	1. 也可以接收一个key函数来实现自定义的排序
		sorted(L, key = abs)
	2.反向排序，不必改动key函数，可以传入第三个参数reverse=True

	3.练习
		L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]  按名字排序

8.返回函数

9.匿名函数
	a.匿名函数也是一个函数对象
	b.f = lambda x: x * x
	c.也可以把匿名函数作为返回值返回
		return lambda: x * x + y * y

10.装饰器 : 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
	a.由于函数也是一个对象，而且函数对象可以被赋值给变量，
		所以，通过变量也能调用该函数
	b.f.__name__
	c.OOP的装饰模式需要通过继承和组合来实现
	d.Python的decorator可以用函数实现，也可以用类实现。
11.偏函数 Partial function
	a.把一个函数的某些参数给固定住（也就是设置默认值），
		返回一个新的函数，调用这个新函数会更简单
  



