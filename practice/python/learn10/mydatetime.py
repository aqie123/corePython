from datetime import datetime

now = datetime.now()

print(now)

# 如果仅导入import datetime，则必须引用全名datetime.datetime。

# 指定时间
dt = datetime(1993,1,16,12,24,35);
print(dt)

# datetime转换为timestamp

print(now.timestamp())
my = dt.timestamp()
print(my)

# timestamp转换为datetime
print(datetime.fromtimestamp(my))
# timestamp也可以直接被转换到UTC标准时区的
print(datetime.utcfromtimestamp(my))


'''
timestamp是一个浮点数，它没有时区的概念，
而datetime是有时区的
本地时间是指当前操作系统设定的时区。
实际上就是UTC+8:00时区的时间
2015-04-19 12:20:00 UTC+8:00
'''


# str 转换为datetime
cday = datetime.strptime('2017-09-09 08:24:10', '%Y-%m-%d %H:%M:%S')
print(cday)


# datetime转换为str
now = datetime.now()
print(now.strftime('%y-%m-%d %H:%M'))


# datetime加减
from datetime import timedelta
now = datetime.now()
now + timedelta(hours = 10)
now + timedelta(days=2, hours=12)
