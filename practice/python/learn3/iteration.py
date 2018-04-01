L = list(range(8))
# for x in L:
	# print(x)

d = {'a': 1, 'b': 2, 'c': 3}
for y in d:
	print(y)

for value in d.values():
	print(value)

for y in "aqie456":
	print(y)

for i, value in enumerate(L):
	print(i, value)

for i, value in enumerate(d):
	print(i, value)

M = []
for i in list(range(1,10)):
	M.append(i * i)
print(M)



A = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
B = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']

print([m + n for m in 'ABC' for n in 'XYZ'])
print([x + y for x in A for y in B])

for k,v in d.items():
	print(k ,"=>", v)

c = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in c if isinstance(s, str)])

def Fibonacci(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1
	return "done"

g = Fibonacci(5)
while True:
	try:
		x = next(g)
		print(x)
	except StopIteration as e:
		print("Generator return value:", e.value)
		break

# 杨辉三角

def PascalTriangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[x] + L[x+1] for x in range(len(L)-1)] + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break 
