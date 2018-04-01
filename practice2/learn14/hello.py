# 实现Web应用程序的WSGI处理函数
# server.py，负责启动WSGI服务器，加载application()函数
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text-html')])
	body = '<h1>Hello %s</h1>' % (environ['PATH_INFO'][1:] or 'Web')
	return [body.encode('utf-8')]