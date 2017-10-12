# 如何构建xml
'''
解决：
xml.etree.ElementTree 构建Element 使用write写入
'''

from xml.etree.ElementTree import Element,ElementTree,tostring

# 构造器接收字符串
e = Element('Data')
# 获取属性
e.tag

# 添加属性
e.set('name','aqie')

tostring(e)    # b'<Data name="aqie" />'

# 添加内容
e.text='aqie'
tostring(e)

# 添加子元素
e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
e2.append(e3)

tostring(e2)

e.text = None
e.append(e2)
tostring(e)

# 写入放到文件
et = ElementTree(e)
et.write('aqie.xml')


'''
import csv
from xml.etree.ElementTree import Element,ElementTree,tostring
from tools import pretty
def csvToXml(fname):
    with open(fname, 'r') as f:
        # 读取头部信息
        reader = csv.reader(f)
        headers = reader.next()

        # 创建根节点
        root = Element('Data')
        for row in reader:
           eRow = Element("Row")
           root.append(eRow)
           for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                e.Row.append(e)
    pretty(root)
    return ElementTree(root)

et = csvToXml('pingan.csv')
et.write('pingan.xml')
'''
