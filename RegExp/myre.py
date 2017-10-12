#!/usr/bin/env python3
import re 

mystr = 'aooooooooooooooabaabbbbbbabaqie123'
regex = '.*?(a.*?a).*'
m = re.match(regex, mystr)
if m is not None:
	print(m.group())