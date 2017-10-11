# 如何解析简单xml文档
'''
解决: xml.etree.ElementTree模块 parse() 解析xml文档
'''
from xml.etree.ElementTree import parse
f = open('demo.xml')
et = parse(f)
root = et.getroot()

# 标签
root.tag
# 属性
root.attrib

root.text.strip()  # 过滤掉空白字符

root.getchildren()

# root 是个可迭代对象
for child in root:
	print(child)     # 获取节点属性

# 查找节点
root.find('body')

# 查找节点为可迭代对象
root.iterfind('body')
for e in root.iterfind('body'):
	print(e.get('name'))


# 查找当前节点所有元素
list(root.iter())

list(root.iter('rank'))