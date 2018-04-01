# Base64是一种用64个字符来表示任意二进制数据的方法
# (任意二进制到文本字符串的编码方法)
# 二进制数据进行处理，每3个字节一组，
# 一共是3x8=24bit，划为4组，每组正好6个bit：
# 4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串
import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

# +和/分别变成-和_
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')

# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容

'''
数据不是3的倍数，最后会剩下1个或2个字节怎么办？
Base64用\x00字节在末尾补足后，
再在编码的末尾加上1个或2个=号，表示补了多少字节，
解码的时候，会自动去掉。
'''

base64.b64encode(b'abcd')  
base64.b64decode('YWJjZA==')     # 长度永远是4的倍数

# 处理去掉=base64解码函数
def safe_base64_decode(s):
	slen = len(s)
	# 补齐 4-slen % 4 个等号
	n = 4 - (slen % 4)
	while n > 0:
		n = n -1
		s += "="
	return base64.b64decode(s)

print(safe_base64_decode('YWJjZA'))
