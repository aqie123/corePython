
# 删掉偶数，只保留奇数
A = list(range(1,10))
print(A)
def is_odd(n):
	return n % 2 == 1

B = list(filter(is_odd, A))
print(B)

# 序列中的空字符串删掉 
# strip() 方法用于移除字符串头尾指定的字符 默认空格
A =  ['A', '', 'B', None, 'C', '  ']
def not_empty(s):
	return s and s.strip()

B = list(filter(not_empty, A))

print(B)