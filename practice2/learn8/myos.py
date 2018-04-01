# 文件操作

import os
print(os.name)	# nt

# 环境变量
# print(os.environ)
# print(os.environ.get('PATH'))

# 查看当前目录的绝对路径:
# print(os.path.abspath('.'))	# D:\python\learn8

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('D:/python/learn8', 'aqie.txt')

# 然后创建一个目录:
# os.mkdir('D:/python/learn8/aqie.txt')

# 删除一个目录
# os.rmdir('D:/python/learn8/aqie')

# os.path.split()函数  拆分字符串

# os.path.splitext()可以直接让你得到文件扩展名


# 文件重命名
# os.rename('aqie.txt', 'aqie.php')

# 删除文件
# os.remove('aqie.php')

# 列出当前目录下的所有(目录)
L = [x for x in os.listdir('.') if os.path.isdir(x)]
print(list(L))

# 列出所有的.py文件
L = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(L)