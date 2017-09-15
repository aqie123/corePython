'''
简单Telent客户端
TelentClient.py
'''
from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque

class TelnetClient(object):
	"""docstring for TelnetClient"""
	def __init__(self, addr, port=23):
		self.addr = addr
		self.port = port
		self.tn = None

	# 连接对象
	def start(self):
		# 人为抛出异常
		raise Exception('Telnet Exception')

		#user
		t = self.tn.read_until('login: ')
		stdout.write(t)
		user = stdin.readline()
		self.tn.write(user)

		#password
		t = self.tn.read_until('Password: ')
		if t.startswith(user[:-1]): t = t[len(user) + 1:]
		stdout.write(t)
		self.tn.write(stdin.readline())

		t = self.tn.read_until('$ ')
		stdout.write(t)
		while True:
			uinput = stdin.readline()
			if not uinput:
				break
			self.history.append(uinput)
			self.tn.write(uinput)
			t = self.tn.read_until('$ ')
			stdout.write(t[len(uinput) + 1:])


	def cleanup(self):
		pass

	# 实现上下文管理
	def __enter__(self):
		# 创建连接
		self.tn = Telnet(self.addr, self.port)
		# 队列存储用户历史记录
		self.history = deque()
		return self
	def __exit__(self, exc_type,exc_val, exc_tb):
		print('IN __exit__')
		self.tn.close()
		self.tn = None
		with open(self.addr + '_history.txt', 'w') as f:
			f.writelines(self.history)
		# return True  返回真值，会输出END


'''
client = TelnetClient('127.0.0.1')
print('\nclient start ...')

client.start()
print('\n cleanup')
client.cleanup()
'''

with TelnetClient('127.0.0.1') as clinet:
	client.start()

print('END')