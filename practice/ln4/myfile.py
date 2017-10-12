# 如何读写文本文件
'''
python2 字符串 str unicode
写入文件前对unicode编码，读入文件后对二进制字符串解码
python3        bytes  str
open函数指定t 文本格式，encoding指定编码格式
'''
s= '啊切'         # python2 前面才带u
s.encode('utf8')  # 得到string字符串  b'\xe5\x95\x8a\xe5\x88\x87'
s.encode('gbk')   # b'\xb0\xa1\xc7\xd0

print(b'\xe5\x95\x8a\xe5\x88\x87'.decode('utf8'))

f = open('note.md', 'w', encoding='utf8')    # t 默认，可忽略
f.write('测试输出')
f.close()

f = open('note.md', 'r', encoding='utf8') 
s = f.read()
f.close()