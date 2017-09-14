# 如何读写json数据
import json



d = {'b':None,'a':'sss'}
d = json.dumps(d,separators=[',',':'])

# 对输出字典中的键进行排序
e = json.dumps(d,sort_keys=True)

# json字符串转换为json对象
jstr = '{"a": "sss", "b": null}'

jstr = json.loads(jstr)

# load 接口是文件
l = [1,'3','ds',{'name':'Bob','age':13}]
l = json.dumps(l)

# 这里使用w而非wb     a bytes-like object is required, not 'str'
with open('demo.json','w') as f:
	 json.dump(l,f)

with open('demo.json','r') as f:
	myjson = json.load(f)
	