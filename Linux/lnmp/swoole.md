1.查看端口状况 (https://linux.cn/article-2434-1.html)

	2.netstat –apn 查看进程列表
	3. 显示进程 ： ps -ef  ps -aux
	4. 端口号是否被占用 netstat -anp|grep 66666 
	5. netstat -paut 查看本机socket端口详细信息
	6.netstat -ant  查看tcp连接
	7. netstat -atunlp

2. 查看程序执行端口
	1. ps -ef|grep php  (UID       PID   PPID     C STIME   TTY    TIME     CMD)
	   ps -ef|grep xxx.php
	2. netstat -anp|grep 886  检查端口
	3.杀死进程 kill 4830 pid  
3.
	1. ps -ef|grep nginx 查看nginx是否启动
	2. netstat -luntp|grep nginx  查看 nginx监听端口