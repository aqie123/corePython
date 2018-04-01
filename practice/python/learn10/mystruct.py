# b'str'可以表示字节
# pack函数把任意数据类型变成bytes
import struct
struct.pack('>I', 10240099)

# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# I：4字节无符号整数和H：2字节无符号整数。
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

'''
两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
'''

a = struct.unpack('<ccIIIIIIHH', s)
# print(a)

# 判断一个文件是否是位图文件
import os
def bmpinfo(file):
	try:
		if os.path.isfile(file):
			with open(file, 'rb') as f:

				bThirty = f.read(30)

				if len(bThirty) < 30:
					print("not不是位图文件")
					return 
				infos = struct.unpack('<ccIIIIIIHH', bThirty)
				if infos[0] != b'B' or infos[1] != b'M':
					print("不是位图文件!")
					return
				print('The bmp file is %s * %s , and colors are %s' % (infos[6], infos[7], infos[9]))
		else:
			print("文件不存在")
	except Exception as e:
		print(str(e))
		print('粗错啦！！！')

bmpinfo("D:\python\\a.bmp")
