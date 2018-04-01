一： HTTP协议
	1.一个HTTP请求只处理一个资源
	2.Apache、Nginx、Lighttpd
二: web应用
	a.不希望接触到TCP连接、HTTP原始请求和响应格式
	浏览器发送一个HTTP请求；

	服务器收到请求，生成一个HTML文档；

	服务器把HTML文档作为HTTP响应的Body发送给浏览器；

	浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。
三： 接口WSGI：Web Server Gateway Interface

四：web框架
	1.pip install flask