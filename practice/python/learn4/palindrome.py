# 回数是指从左向右读和从右向左读都是一样的数
def is_palindrome(n):
	n = str(n)
	return n == n[::-1]

output  = filter(is_palindrome,range(1,100))
print(list(output))