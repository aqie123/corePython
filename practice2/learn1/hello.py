#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(ord('z'))
print(chr(53))
# name = input('please enter your name')
# print('hello 啊切', name)
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('%.1f%%' % r)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

for y in list(range(101))
	sum = sum + y
print(sum)