'''
问题：
1.访问二进制文件，希望把文件映射到内存，实时访问
(linux 的 framebuffer 设备文件)
2.嵌入式设备，寄存器编址到内存地址空间
  映射到/dev/mem某范围，访问这些寄存器
3.多个进程映射到同一个文件，实现进程通信


解决：
mmap模块 mmap(文件描述符)

dd if=/dev/zero of=demo.bin bs=1024 count=1024    创建文件
od -x demo.bin 查看文件

'''

import os,mmap

# os.open 有文件描述符
f = open('demo.bin','r+b')

# 映射区域大小 0代表整个文件
# f.fileno 得到文件描述符
# 访问权限

m = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)

# type(m)  # mmap.mmap 对象, ；类似数组操作 m[0] = '\x00' 返回字节形式0
# m[10:20] 可以切片操作


#offset 以内存页 映射八个页
m = mmap.mmap(f.fileno(),mmap.PAGESIZE * 8,access=mmap.ACCESS_WRITE,offset=mmap.PAGESIZE * 4)