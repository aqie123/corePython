# 处理二进制文件
# wav 前44字节音频文件信息
f= open('demo.wav','rb')
info = f.read(44)

import struct
'''
struct.unpack('h', b'\x01\x02')     (513,)
struct.unpack('>h', b'\x01\x02')	(258)

x = [1 for i in range(5)]     [1, 1, 1, 1, 1]
x = [1 for _ in range(5)]
'''
struct.unpack('h', info[22:24])     # 声道数 2
struct.unpack('i', info[24:28])     # 采样频率 (44100,)
struct.unpack('h', info[34:36])     # 编码宽度 (16,)

# 得到数组长度   (文件长度-44)/2
import array

f.seek(0,2)     # 文件指针移动到末尾   2219096
n = (f.tell() - 44)/2
n = int(n)
# 生成器表达式初始化数组
buf = array.array('h', (0 for _ in range(n)))

# 指针指向数据部分
f.seek(44) 

# 文件数据读取到buf
f.readinto(buf)

# buf[10]

for i in range(n):
	buf[i]/8

# 将数据写入到新文件
f2 = open('demo2.wav','wb')
f2.write(info)

# 将buf中信息写入到文件,传一个对象
buf.tofile(f2)
f2.close()

'''
open以二进制模式打开文件
二进制数据以readinto,读入到buffer中
解析二进制数据使用标准库中struct模块unpack方法

'''