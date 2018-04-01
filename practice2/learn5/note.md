# 模块
	1.导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，
		就可以访问sys模块的所有功能。
	2.sys模块有一个argv变量，用list存储了命令行的所有参数。
	  argv至少有一个元素，因为第一个参数永远是该.py文件的名称
	3.行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，	

	  而如果在其他地方导入该hello模块时，if判断将失败，
	4.hello.test()  调用

	5.安装模块 pip install Pillow
# 面向对象 (Object Oriented Programming)
	1. 类（Class）和实例（Instance）

  2.继承和多态
  3.开闭原则
    对扩展开放：允许新增Animal子类；

    对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
  4. 获取对象信息
    a.type(123)
    b. type(fn)==types.FunctionType 
    c. type(abs)==types.BuiltinFunctionType 
    d. type(lambda x: x)==types.LambdaType 
    e. type((x for x in range(10)))==types.GeneratorType
    f. dir('Aqie') 获取对象所有属性和方法
  5. from type import MyObject  引入对象

  6. 实例属性和类属性

  7.面向对象高级编程 
    1.基本 ： 封装，继承 多态
    2.多重继承 ，定制类，元类
    3. __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    4.子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
    5. 既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
      内置的@property装饰器就是负责把一个方法变成属性调用的
  8. 多重继承 ： 一个子类就可以同时获得多个父类的所有功能
  
  9.定制类

  10.枚举类
    1. 问题： 定义常量 DEC = 12  (缺点是类型是int，并且仍然是变量)
    2. 解决： 枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例
    3.Enum派生出自定义类

  11. 使用元类
    1.静态语言; 函数和类的定义，不是编译时定义的，而是运行时动态创建的
    2.使用type()动态创建类
    3.使用元类创建类
      metaclass
      __new__()方法接收到的参数依次是：

      当前准备创建的类的对象；

      类的名字；

      类继承的父类集合；

      类的方法集合。

  12.应用：
    ORM全称“Object Relational Mapping”，即对象-关系映射，
    就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表