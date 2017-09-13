# 调整字符串中文本格式
# 应用：log文件日期格式 yyyy-mm-dd  -> yy/mm/dd
# 解决：正则表达式捕获组

log = open('./test/my.log', encoding= 'utf-8').read()
import re

# mylog = re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)      # 捕获组带括号

# 给每个组起名字
mylog = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',log)      
'''
后面替换用原始字符串
r'\1'	'\\1'
'\1'	'\x01'
len('\1')   1
'''

print(mylog)