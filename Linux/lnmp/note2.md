一：SELinux
	1.查看SELinux状态：
		/usr/sbin/sestatus -v 
	2.临时关闭
		setenforce 0  成为permissive模式
   		setenforce 1  成为enforcing模式
	3.永久关闭(重启需要)
		/etc/selinux/config 文件 
		SELINUX=enforcing改为SELINUX=disabled
二：ss(http://note.youdao.com/share/?id=7f8290d924942d2e5a839d5b3bfcbef2&type=note#/)
	1. pip install shadowsocks
	2. 把/usr/local/bin加入到/etc/profile
	3. mkdir /etc/shadowsocks
	4. vim /etc/shadowsocks/config.jsons
	5.启动 ssserver -c /etc/shadowsocks/config.json -d start
	6.netstat -tunlp
	7.关闭 ssserver -c /etc/shadowsocks/config.json -d stop

	8.windows客户端下载
		https://github.com/shadowsocks/shadowsocks-windows/releases
三：Linux 上安装和配置 Munin 监控服务器
	http://www.448569.gove.cn/article/516199.html
四：