# 使用临时文件
'''
问题：
传感器采集数据，每收集到1g数据，数据分析，最终
只保存分析结果，临时文件常驻内存，消耗内存资源
使用临时文件存储临时数据(外部存储)
临时文件不用命名,关闭后自动被删除

解决:
tempfile模块 下 TemporaryFile, NamedTemporaryFile
'''
from tempfile import TemporaryFile, NamedTemporaryFile

# TemporaryFile(mode='w+b', bufsize=-1, suffix='', prefix='tmp',dir=None)



# 得到临时文件对象,只能通过对象f访问，无法在系统路径找到
f = TemporaryFile()

# 临时数据放入到临时文件
f.write(b'abcdef' * 100000)

# 读取临时数据,操作文件指针
f.seek(0)

# 根据需求，每次读入
f.read(100)

#-------------------------
# NamedTemporaryFile(mode='w+b', bufsize=-1, suffix='', prefix='tmp',dir=None,delete=True)

# 每次重新创建，垃圾回收会自动删除文件
ntf = NamedTemporaryFile()
ntf.name   #'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\tmpt1fowr0q'

