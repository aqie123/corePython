#!/usr/local/bin/python3

from mylib.myregex import sayhello
from mylib.myregex import matchone
from mylib.myregex import searchone

sayhello()

line = 'there is food on the table'
reg = '(foo)'
matchone(line, reg)
searchone(line, reg)
