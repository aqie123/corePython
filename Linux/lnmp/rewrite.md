1.https://segmentfault.com/a/1190000002797606

一：Rewrite
	1.  所有的请求重定向到一个页面
		rewritr ^(.*)$/pages/maintain.html break;
二：正则表达式
	1. . 除换行符以外任意字符
	   ?   重复0次或一次
	   +   重复一次或更多次
	   *   最少连接数,那个机器连接数少就分发
	   \d  数字
	   ^   匹配字符串开始
	   $   匹配字符串结束
	   {n}  重复n次
	   {n,} 重复n次或更多次
	   [c]  匹配单个字符c
	   [a-z]  a-z任意小写字母
	2.
		\ 转义字符  \.
		()  用于匹配括号间内容，用$1,$2调用
		pcretest
		if($http_user_agent ~ NSIE){
			rewrite ^(.*)$ /msie/$1 break;
		}
	3.pcre使用
		1. /(\d+)\.(\d+)\.(\d+)\.(\d+)/
	4.	   last 停止rewrite检测
		   break 停止rewrite检测
		   redirect 返回302临时重定向,地址栏显示跳转后地址
		   permanent 返回302永久重定向,地址栏显示跳转后地址
	5.
		1. http://192.168.144.128:92/last/
		2. last 相比 break 会重新建立一个请求 请求以test开头
		3. curl -vL  http://192.168.144.128:92/test/
			redirect 和last相比会多个302  发起两次请求
		4. 
			redirect 302   
			permanent 301 永久重定向服务器关闭也会跳转
	6. 目录分级
		1.
			目录 ：/home/aqie/phpApi/code6/course/11
			地址： http://192.168.144.128:92/course/11/html/course_33.html
			改写 ： http://192.168.144.128:92/course-11-html-33.html
	7.优先级
		1. server > location > location 中 rewrite
	8.优雅：
		1.
			server_name nginx.org;
			rewrite ^ http://www.nginx.org$request_uri?
		2. 