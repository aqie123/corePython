#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 找出文章中出现频度最高的词

import re      # 导入正则表达式
from collections import Counter

txt = open('english.txt').read()
# print(txt)
c3 = Counter(re.split('\W+', txt))

print(c3.most_common(10))