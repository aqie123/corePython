# 猜数字游戏
from random import randint
from collections import deque
import pickle

N = randint(0, 100)
history = deque([],5)

def guess(K):
	if K == N:
		print('you got it')
		return True
	if K < N:
		print('%s is less than N' % K)
	if K > N:
		print('%s is greater than N' % K)

while True:
	line = input('Please input a numebr between 0-100: ')
	if line.isdigit():
		k = int(line)
		history.append(k)
		pickle.dump(history,open('history','wb'))
		if guess(k):
			break
	elif line == 'history' or line == 'h':
		print(list(history))

'''
s为字符串
s.isalnum() 所有字符都是数字或者字母
s.isalpha() 所有字符都是字母
s.isdigit() 所有字符都是数字
s.islower() 所有字符都是小写
s.isupper() 所有字符都是大写
s.istitle() 所有单词都是首字母大写，像标题
s.isspace() 所有字符都是空白字符、\t、\n、\r
'''

# 容量为n队列存储，deque 双端循环对列
# (队列： 前删后增)
# 程序退出前，history对象存储到文件中
# pickle.dump？
# history = pickle.load(open('history','rb'))     #读取历史记录
# history = open('history','r', encoding='UTF-8')
