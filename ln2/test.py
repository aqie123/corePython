def f():
	print('in f(), 1')
	yield 1

	print('in f(), 2')
	yield 2

g = f()
# print(next(g))
# print(next(g))
for x in g:
	print(x)