# 字典字符串左中右居中对齐
# 方法一：str.ljust() str.rjust()  str.center()
# s.ljust(width[,fillchar])

d = {'DistCull':500.00,'SmallCull':0.04,'farclip':477,'lodDist':100.0,
'trilinear':40}

w = max(list(map(len,d.keys())))   #最大宽度
for k in d:
    print(k.ljust(w),":",d[k])




# 方法二：format() 传递 '<20' '>20' '^20'
# format(s, '<20') 左对齐
for k in d:
    print(format(k,'<9'), ':', d[k])