# 服务端TCP(ransmission Control Protocol )编程

# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
# 如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，
# 随后的通信就靠这个Socket连接了。

#：服务器地址、服务器端口、客户端地址、客户端端口确定一个Socket


# 基于IPv4和TCP协议的Socket
import socket,threading,time
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口
s.bind(('127.0.0.1', 9999))

# listen()方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print('Wating for connection')

# 服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
while True:
    # 接收一个新连接
    sock, addr = s.accept()
    # 创建新线程处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

# 每个连接都必须创建新线程（或进程）来处理
