# 文件对象的缓冲
'''
问题： 文件写入硬件设备,使用系统调用,
I/O操作时间很长,减少I/O操作次数
文件通常使用缓冲区 (凑够块大小才使用缓冲)
缓冲区大小 4096
全缓冲，open 函数 buffering 设置为大于一整数n,n为缓冲区大小
行缓冲，open buffering 设置为1
无缓冲  open buffering 设置为0
'''
f = open('demo.txt','w')

f.write('+' * 2045)
f.close()

# 全缓冲修改缓冲区大小    tail -f demo2.txt  监测文件
f2 = open('demo2.txt','w',buffering=2048)
f2.write('a' * 2047)
f2.write('aqie')
f2.close()


# 行缓冲
f3 = open('demo3.txt','w',buffering=1)
f3.write('aqie123')
f3.write('\n')
f3.close()


