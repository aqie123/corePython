# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，
# 优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，
# 缺点是我们需要自己处理事件。

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHtmlParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)

	def handle_endtag(self, tag):
		print('</%s>' % tag)

	def handle_startendtag(self, tag):
		print('<%s/>' % tag)

	def handle_data(self, data):
		print(data)

	def handle_comment(self, data):
		print('<!--', data, '-->')

	def handle_entityref(self,name):
		print('&%s;'  % name)

	def handle_chaeref(self, name):
		print('&#%s;'  % name)


parser = MyHtmlParser()
parser.feed(
'''

'''

)