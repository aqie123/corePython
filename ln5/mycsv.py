# 读写csv文件
'''
问题：
雅虎网站获取中国股市数据集。以csv格式存储
http://table.finance.yahoo.com/table.csv?s=000001.sz

成交量超过500000000存储到另一个csv文件

解决：
csv模块 reader和 writer完成csv文件读写
'''
# 导入下载模块
import urllib.request
urllib.request.urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz',
 'pingan.csv')

import csv
rf = open('pingan.csv', 'rb')

# reader 是一个迭代器
reader = csv.reader(rf)  

reader.next()

#--------------
'''
writer.dialect
writer.writerow
writer.writerows
'''

wf = open('pingan_copy.csv','wb')
writer = csv.writer(wf

# 写入一行
writer.writerow(['Date','Open','High','Low','Close','Volume','Adj close'])

# 边读边写
writer.writerow(reader.next())
wf.flush()


# 编写脚本
'''
import csv
with open('pingan.csv','rb') as rf:
	reader = csv.reader(rf) 
	with open('pingan2.csv','rb') as rf:
		writer.writerow(wf)
		# 头部写入
		headers = reader.next()
		write.writerow(headers)
		for row in reader:
			if row[0] < '2016-01-01':
				break
			if row[5] >= 50000000:
				writer.writerow(row)
print('end')
'''