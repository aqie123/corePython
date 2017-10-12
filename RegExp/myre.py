#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import re
from mylib.myregex import matchone
from mylib.myregex import searchone
from mylib.myregex import findall
from mylib.myregex import finditer
from mylib.myregex import sub
from mylib.myregex import split
from mylib.myregex import forL
from mylib.commonfuc import mytime
from mylib.commonfuc import foo
from mylib.mydecorator import dictsplit

line = 'aooooooooooooooabaabbbbbbabaqie123'
reg = '.*?(a.*?a).*'
matchone(reg, line)

line = 'you bite me'
reg = 'bit'
searchone(reg, line)

line = 'c3po'
reg = '[cr][23][dp][o2]'
matchone(reg,line)

line = 'knsnakmk'
reg = '\w+'
matchone(reg,line)

# 匹配任意网址 protocol :// hostname[:port] / path / [;parameters][?query]#fragment
line = 'www.baidu.com'
# reg = '\w+(@\w)?+\.\w+\.com'
reg = '\w+\.\w+\.com'
matchone(reg,line)

line = 'https://zhidao.baidu.com/question/524627668.html'
reg = '(http|https)://\w+\.(\w+\.)?com/\w+/\w+\.(html|php)'
matchone(reg,line)

# \b只能匹配字母、数字、汉字、下划线
line = 'bite the dog'
reg = r'\bthe'
searchone(reg, line)

line = 'hi, his history score is high'
reg = r'\bhi\b'
searchone(reg, line)

findall('car', 'carry the barcardi to the car')

line = 'This and that'
reg = r'(th\w+) and (th\w+)'
findall(reg, line, re.I)

finditer(reg, line, re.I)

reg = r'(th\w+)'
findall(reg,line, re.I)

sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
sub('[ae]', 'X', 'abcdefg')

# MM/DD/YY{,YY}  DD/MM/YY{,YY} 10/12/2017 1991/02/20
sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3','10/12/2017')

split(':','name:aqie')

l = [1,2,3,4,5]

forL(l)

mytime()

"""
*args表示任何多个无名参数，它是一个tuple；
**kwargs表示关键字参数
"""
foo(1,2,3, name='aqie', age=18)

print(foo.__name__)

# 输入城市和州名，或者城市名加上 ZIP 编码，还是三者同时输入
Data = (
    'Mountain View, CA, 28232 ',
    'Sunghd,LG',
    'Los Altos, 39926',
    'Palo Alto CD'
)
for a in Data:
    split(', |(?=(?:\d{5}|[A-Z]{2}))', a)































