# 导入socket库:(客户端)
import socket

# 创建一个socket对象:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))

'''
AF_INET指定使用IPv4协议，
如果要用更先进的IPv6，就指定为AF_INET6。
SOCK_STREAM指定使用面向流的TCP协议，
'''

# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# TCP连接创建的是双向通道

buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# 把接收数据写入文件
with open('sina.html', 'wb') as f:
	f.write(html)