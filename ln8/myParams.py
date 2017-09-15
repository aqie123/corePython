# 如何定义带参数装饰器
'''
装饰器用来检查被装饰函数的参数类型
装饰器可通过参数指明函数参数的类型
如果检测出类型不匹配则抛出异常
@typeassert(str, int, int)
def f(a,b,c):

@typeassert(y=list)
def g(x,y):

解决：
   带参数装饰器，根据参数定制化一个装饰器，
   看成生产装饰器工厂，每次调用typeassert,
   返回一个特定装饰器，然后它去修饰其他函数
'''

# 获取函数参数签名
from inspect import signature

'''
def f(a,b,c = 1): pass
sig = signature(f)
sig.parameters

#建立字典
bagrs = sig.bind(str, int, int)

# sig.bind_partial  指定某些参数设置类型

bagrs.arguments
# OrderedDict([('a', <class 'str'>), ('b', <class 'int'>), ('c', <class 'int'>)])

bagrs.arguments['a'] 
#str

'''

def typeassert(*ty_args, **ty_kargs):
    # 真正装饰器函数
    def decorator(func):
        # 获取函数参数和它映射关系
        '''
        func -> a,b
        d = {'a':int, 'b':str}
        '''
        sig = signature(func)
        # 部分绑定
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments
        def wrapper(*args, **kargs):
            # arg in d,instange(arg, d[arg])
            for name,obj in sig.bind(*args, **kargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"%s" must be "%s"' % (name, btypes[name]))
            return func(*args, **kargs)
        return wrapper
    return decorator

@typeassert(int,str,list)
def f(a,b,c):
    print(a,b,c)

f(1,'abc',[1,'aqie'])

# 下面会报错，perfect
f('abc','aqie','name')