
# str 写入 StringIO
from io import StringIO
f = StringIO()
f.write('hello')
f.write('aqie')
print(f.getvalue())

# 读取StringIo 用一个str初始化StringIO，然后，像读文件一样读取
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

# BytestIo 读取二进制文件
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())