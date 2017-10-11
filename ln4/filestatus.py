# 访问文件的状态
'''
1.文件类型(普通文件,目录,符号链接,设备文件)
2.文件的访问权限
3.文件的最后访问/修改/节点状态更改时间 (read, write, chande mode)
4.普通文件大小


解决办法：
1.系统调用：os 模块三个系统模块 stat fstat lstat
2.快捷函数 os.path下的函数(推荐)

'''
import os

f = open('demo.txt','w')
os.fstat(f.fileno())   # 传入描述符

# 获取文件状态
s = os.stat('demo2.txt')

# 转换成二进制
bin(s.st_mode)

# stat.  
import stat
stat.S_ISDIR(s.st_mode)     # 传入mode值,判断是否是文件

# 判断是否是普通文件
stat.S_ISREG(s.st_mode)

# 文件权限 
# R读的权限 (USR 用户, GRP 组 OTH 其他)  256 > 0就是真
s.st_mode & stat.S_IRUSR    

# 执行权限
s.st_mode & stat.S_IXUSR        # 0 

# 文件最后访问时间
import time
time.localtime(s.st_atime)
s.st_atime

# 普通文件大小
s.st_size


#————————————————————os.path——————————————————————————————

# 判断是否是目录
os.path.isdir('demo.txt')

# 是否是符号链接
os.path.islink('demo.txt')

# 是否是普通文件
os.path.isfile('demo.txt')

# 三个时间
os.path.getatime('demo.txt')

# 文件大小
os.path.getsize('demo.txt')