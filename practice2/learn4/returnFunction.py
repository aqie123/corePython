
A = [36, 5, -12, 9, -21]
# 定义普通求和函数
def my_sum(L):
	sum = 0
	for x in L:
		sum = sum + x
	return sum

print(my_sum(A))


# 返回求和的函数  (闭包)
def lazy_sum(*args):
	def sum():
		res = 0
		for x in args:
			res = x + res
		return res
	return sum

a = lazy_sum(1,2,3)
# a 是一个求和函数
print(a())

# 返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

#解决
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs