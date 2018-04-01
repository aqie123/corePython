# 1.列出从2开始的所有自然数，构造一个序列

# 2.取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# begin

# 1.构建3开始的奇数队列 generator
def _odd_iter():
	n = 1
	while True:
		n = n+2
		yield n

# 然后定义一个筛选函数：

def _not_divisible(n):
    return lambda x: x % n > 0

# 最后，定义一个生成器，不断返回下一个素数：

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# primes()也是一个无限序列，

# 打印1000以内的素数:  Iterator是惰性计算的序列，
for n in primes():
    if n < 100:
        print(n)
    else:
        break