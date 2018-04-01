import os
from datetime import datetime
import sys

# 实现 dir -l
mypath = os.path.abspath('.')
# 返回当前目录
# print(os.curdir)
# 获取当前工作目录
# print(os.getcwd)
# 列出指定目录下的所有文件和子目录
# print(os.listdir(mypath))
'''
引发一个 SystemExit异常，若没有捕获这个异常，
Python解释器会直接退出；捕获这个异常可以做一些额外的清理工作。0为正常退出
其他数值可抛异常事件供捕获
多用于主线程退出
'''
# sys.exit(0)

# os._exit() 直接退出 Python程序，其后的代码也不会继续执行,用于线程中退出
print('      Size     Last Modified  Name')
print('------------------------------------------------------------')
def mydir(mypath):
	for file in os.listdir(mypath):
		fsize = os.path.getsize(file)
		mtime = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M')
		flag = '/' if os.path.isdir(file) else ''
		print('%10d %s %s%s' % (fsize, mtime, file, flag))
		
mydir(mypath)