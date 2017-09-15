'''
实现属性可修改的函数装饰器
为分析程序内哪些函数执行时间开销大，定义
带timeout参数的函数装饰器：
1，统计被装饰函数单词调用运行时间
2，时间大于参数timeout,将此次函数调用记录到log日志
3，运行时可修改timeout值


'''
from functools import wraps
import logging
import time

def warn(timeout):
    '''
    python2变为可变对象 timeout = [timeout]
    之后通过 timeout[0] 来访问,只有一项列表
    '''
    def decorate(func):
        def wrapper(*args, **kargs):
            start = time.time() 
            res = func(*args, **kargs)
            used = time.time() - start
            if used > timeout:
                msg = '"%s" : %s > %s' % (func.__name__,used,timeout)
                logging.warn(msg)
            return res
        # 动态修改timeout
        def setTimeout(k):
            # 类似global 声明嵌套语句下变量
            nonlocal timeout
            timeout = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorate


from random import randint
@warn(1.5)
def test():
    print('In test')
    while randint(0,1):
        time.sleep(0.5)

# for _ in range(30):
#     test()

test.setTimeout(1)
for _ in range(30):
    test()

'''
python2 不支持关键字

'''