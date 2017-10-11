# 小字符串拼接成大字符串
# 应用： 网络协议自定义UDP协议,将参数按次序收集到列表中
# 解决： 法一：迭代列表通过+拼接
pl = ['<0122>','<32>','<4544>','<656.05>']

s1 = 'abc'
s2 = 'def'
# s1 + s2     # 实际调用str.__add__
s3 = 'ghi'
print(str.__add__(s1,s2))


# 方法二：str.join(更快) 传入可迭代对象
''.join(['abc','123','xyz'])      # 必须是字符串
print(''.join(pl))

# 列表中包含数字
l = ['abc',123,45,'xyz']
''.join([str(x) for x in l])   # 列表解析  []
''.join(str(x) for x in l)    # 生成器表达式  (str(x) for x in l) 