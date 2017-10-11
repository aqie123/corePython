'''
问题：(TelnetClient)
让对象支持上下文管理
eg: with 打开文件

实现了telnet客户端的类,TelnetClient,
调用实例start() 方法启动客户端和服务器交互
交互完毕需调用cleanup(),关闭已连接的socket
以及将操作历史记录写入文件并关闭

让TelentClient 的实例支持上下文管理协议，
替代手工调用cleanup()


解决：
实现上下文管理协议，需定义实例的 __enter__ , __exit__
分别在with 开始和结束时被调用
'''

'''
创建可管理对象属性 (Circle)
面向对象，将方法看做对象接口
直接访问对象属性是不安全的,或者不灵活

但是使用调用方法在形式上不如访问属性简洁
circle.setRadius(5.0) 繁

circle.radius = 5.0  简单

实现 ：形式上属性访问，实际上调用方法
Circle.py

解决：
使用 property函数为类创建可管理属性，
fget/fset/fdel  相应属性访问

'''

'''
如何让类支持比较操作(Rectangle)

实例支持 < > == != 
矩形的类，比较两个矩形实例时，比较的是面积

解决：
使用 functools 下装饰器 total_ordering
'''


'''
使用描述符对实例属性做类型检查 (descriptor, attr)
类似静态语言 c/c++/java 
动态语言解释器无法完成类型检查
p = Person()
p.name = 'Bob'   # 必须是str

要求：
1.对实例变量名指定类型’
2.赋予不正确类型时抛出异常

解决：
实现 __get__, __set__, __delete__
在 __set__ 内使用 isinstance()做类型检查

'''


'''
如何在环状结构中管理内存 (ringlike, datanode)
python中，垃圾回收器通过引用计数回收垃圾对象
某些环状数据结构(树，图),存在对象间循环引用
树的父节点引用子节点，子节点引用父节点
同时del引用父子节点，两个对象不能被立即回收
如何解决此类内存管理问题

解决：
weakref,创建一种能访问对象但不增加引用计数的对象
'''

'''
如何通过实例方法名字的字符串调用方法
三个不同图形类 Circle,Triangle,Rectangle

都有获取图形面积的接口接口名字不同，’实现一个统一获取面积的函数，
使用每种方法名，调用相应类的接口

方案一：使用内置函数getattr,通过名字在实例上获取对象方法，然后调用
方案二：operator下的methodcaller()调用

'''