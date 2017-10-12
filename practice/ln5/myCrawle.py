import re
import urllib.request
###result yes
# version 3.5
def Schedule(a,b,c):
       '''
       a:已经下载的数据块
       b:数据库块的大小
       c:远程文件的大小
       '''
       per = 100.0 * a * b / c
       if per>100:
           per = 100
           print('完成！')
       print('%.2f%%' % per)
def getHtml(url):
       page = urllib.request.urlopen(url)
       html = page.read()
       return html

def getImg(html):
       html = html.decode('utf-8')
       reg = r'src="(.*?\.jpg)" width'
       imgre = re.compile(reg)
       imglist = imgre.findall(html)
       #print(imglist)
       x = 0
       for imgurl in imglist:
              urllib.request.urlretrieve(imgurl,'e:\\test\\%s.jpg' % x,Schedule)#是不是Python3.X中把这个也改变了？
              x += 1

html = getHtml('http://tieba.baidu.com/p/741081023')
print(getImg(html))