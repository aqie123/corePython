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
四：安装ab压力测试
	1.查看apr-util, yum-utils是否安装：
		1.rpm -qa|grep apr-util
		2.rpm -qa|grep yum-utils
	2.yum安装
		1. yum -y install apr-util
		2. yum -y install yum-utils
		3. cd /opt && mkdir abtmp
		4. cd abtmp
		5. yum install yum-utils.noarch
		6. yumdownloader httpd-tools*
		7. rpm2cpio httpd-tools*.rpm | cpio -idmv
		8. cp /opt/abtmp/usr/bin/ab /usr/bin
		9. ab -help
	3. -n 总请求，-c并发数 -k 是否开启长连接
五：Prox 代理
	1. Nginx代理
	2. CDN
	3. 7lay LSB
六： 安装tomcat
	1. cd /opt/app
七。pcretest
	1. rpm -qa pcre  查看pcre包
	2. 查看路径 rpm -ql pcre-8.32-17.el7.x86_64
八。安装pcre2
	3.下载 wget https://ftp.pcre.org/pub/pcre/pcre2-10.23.tar.gz
	4. tar zxvf pcre2-10.23.tar.gz
	5. ./configure --prefix=/usr/local/pcre2-10.23 --libdir=/usr/local/lib/pcre --includedir=/usr/local/include/pcre
	6. 更新动态链接库数据
		echo "/usr/local/lib/pcre" >> /etc/ld.so.conf
		ldconfig -v
	7. ln -s /usr/local/pcre2-10.23/bin/pcre2test /usr/local/bin
		安装完可以无视
九。编译安装pcre
	1.yum -y install make zlib zlib-devel gcc-c++ libtool
	2.
	3.