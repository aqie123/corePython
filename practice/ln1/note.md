1.列表 filter函数 filter(lambda x:x >=0, data)
        列表解析  [x for x in data if x >= 0]
2.字典 字典解析   {k:v for k,v in d.iteritems() if v > 90}
3.集合 几何解析   {x for x in s if x % 3 == 0}


问题： 为元组中元素命名，提高程序可读性
使用元组存储： (存储空间小,访问速度快)