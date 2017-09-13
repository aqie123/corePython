import re

# 正则表达式
s = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
s = re.split(r'[,;|\t]+',s)
print(s)