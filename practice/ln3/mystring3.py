# 如何判断字符串a以字符串b结尾或开头
# 应用： 给所有.sh .py文件加上用户可执行权限
# 解决： str.startswith()  str.endswith() 多个匹配时参数使用元组
import os,stat
files = os.listdir('./test')
# s.endswith(('.h','.py'))   # 接收一个元组，满足一个即为TRUE
print(files)

# 列表解析
files = [name for name in files if name.endswith(('.h','.py'))]
print(files)
print(os.stat('./test/c.h').st_mode)    # 访问文件权限 oct转换为八进制
print(stat.S_IXUSR)   

# 修改文件权限
os.chmod('./test/c.h',os.stat('./test/c.h').st_mode | stat.S_IXUSR)

print(os.stat('./test/c.h').st_mode)   # 访问文件权限 oct转换为八进制
