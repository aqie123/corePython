# 去掉字符串中不需要字符
# 1.过滤空白字符
# 2.过滤windows下的\r    linux  \n   
# 3.去掉文本中的unicode组合符号(音调)

# 解决方法：1.strip,lstrip,rstrip
            # 2.删除单个固定位置字符 切片+拼接
            # 3.字符串replace()或正则re.sub()删除任意位置
            # 4.translate() 同时删除多种不同字符
s = '   abc 234  '
s.strip()       # 指定任意字符在两端删除,默认空格

s='abcd:efgh'
s[:4]+s[-4:]   #s[:4]+s[5:]

s = '\tabc\t123xrf\rops'
s.replace('\t','')

import re
re.sub('[\t\r]','',s)


# 方法四
s  = 'abc1230321xyz'     # abc 和 xyz替换
# str.translate(table,[,deletechars])
# unicode.translate()

# 建立映射表
import string
string.maketrans('abcxyz','xyzabc')  
s.translate(s.maketrans('abcxyz','xyzabc')) 

# 例子2
s = 'abc\refg\n333\t'
# 删除多个字符串
s.translate(s.maketrans('','','\t\r\n'))

# unicode
'''
传入字典
u = 'ā á ǎ à    ō ó ǒ ò'
b = āáǎàōóǒ
u.translate({0x0301:None})
'''