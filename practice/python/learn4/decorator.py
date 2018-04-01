import time
# 装饰器  接收函数

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log   # 相当于执行了语句 now = log(now)
# 只是现在同名的now变量指向了新的函数
def now():
	print(time.time())

now()



# decorator本身需要传入参数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')      # now = log('execute')(now)
def say():
	print('hello aqie')

say()

print(say.__name__)   # 'wrapper'


# 完整装饰器
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 带参数的
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

