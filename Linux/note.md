一： 安装谷歌浏览器
	1.chmod a+w -R /home/PycharmProjects/       ./vmware-install.pl
	2.su root
	3.yum -y install kernel-devel-$(uname -r)
	4.yum install gcc gcc-c++ kernel-devel
	5.查看可以登录系统的用户：cat /etc/passwd | grep -v /sbin/nologin | cut -d : -f 1
	  查看系统中有哪些用户：cut -d : -f 1 /etc/passwd
	6.userdel -rf name  删除用户
	7.rm -rf  /home/git 删除目录
	    rm   /home/git/.ssh   删除文件

	8. 卸载火狐浏览器
		1.yum search 
		2.yum install
		3.rpm -qa | grep firefox查询已安装的旧版firefox
		4.rpm -e firefox-45.4.0-1.el7.centos.x86_64 删除旧版firefox

	9. 安装谷歌浏览器
		1.vim /etc/yum.repos.d/google-chrome.repo
		
		在vim中使用shift+insert粘贴
		
		2.rm -rf /var/run/yum.pid 强行解锁
		3.sudo yum install google-chrome-stable --nogpgcheck
			sudo yum install google-chrome-stable‘
		4.创建快捷方式
			a.cd usr/share/applications
		5.命令行启动
			google-chrome  --user-data-dir

	10. Cannot find a valid baseurl for repo: base/7/x86_64
		1.cd /etc/sysconfig/network-scripts
		2.方法二 dns
			a。vim /etc/resolv.conf 
		3.重启网关 (service network restart)
			a.systemctl status network.service
			b.journalctl -xe

	11. rm /etc/yum.repos.d/google-chrome.repo  删除配置文件

	12.vim /etc/resolv.conf

	13. root 用户启动谷歌
		1.yum list hexedit
		2.yum install hexedit.x86_64
		3. hexedit /opt/google/chrome/chrome  
		4.tab
		5. ctrl +s geteuid
		6.getppid
	14.
		1. shutdown -h now   关机
		2. shutdown -r now   立刻重启
	15. 图形界面切换
		在图形界面使用 ctrl+alt+F2切换到dos界面  

		dos界面 ctrl+alt+F2切换回图形界面

		在命令上 输入 init 3 命令 切换到dos界面 

		输入 init 5命令 切换到图形界面
	16. 查看ip信息
		1.ifconfig
	17.新建文件夹
		1.mkdir /home/aiqe/test
		2.删除文件夹 rm -rf
		3.删除文件   rm -f
	18.cp -r /a  /b      复制a 到b
	   cp /usr/local/nginx/html/php7.tar.gz .  复制到当前目录
	   删除文件 rm -r /usr/local/nginx/html/php7.tar.gz
	   rm -rf /home/test  递归删除目露

二：
	1.配置lnmp
		1.编译安装nginx(http://www.cnblogs.com/hafiz/p/6891458.html)
			a.查看gcc版本 
				gcc -v
			b.yum install gcc-c++
			c.yum install -y pcre pcre-devel
			d.yum install -y zlib zlib-devel
			e.yum install -y openssl openssl-devel

			f.下载nginx源码包
				1.wget http://nginx.org/download/nginx-1.12.0.tar.gz
				2.解压缩：tar -zxvf nginx-1.12.0.tar.gz
				3.cd nginx-1.12.0
				4.新建文件夹
					更改文件夹权限	chmod -R 777 /var   
					mkdir /var/temp /var/temp/nginx /var/run/nginx /var/log/nginx
						  /usr/local/nginx
				5.配置文件

　　　　./configure --prefix=/usr/local/nginx --pid-path=/var/run/nginx/nginx.pid --lock-path=/var/lock/nginx.lock --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --with-http_gzip_static_module --http-client-body-temp-path=/var/temp/nginx/client --http-proxy-temp-path=/var/temp/nginx/proxy --http-fastcgi-temp-path=/var/temp/nginx/fastcgi --http-uwsgi-temp-path=/var/temp/nginx/uwsgi --http-scgi-temp-path=/var/temp/nginx/scgi
				6.--with-http_stub_status_module：支持nginx状态查询
				--with-http_ssl_module：支持https
				--with-http_spdy_module：支持google的spdy,想了解请百度spdy,这个必须有ssl的支持
				--with-pcre：为了支持rewrite重写功能，必须制定pcre
				7.  编译安装
					make && make install
				8. 进入安装目录
					cd /usr/local/nginx/sbin/
				   启动
				   ./nginx
				9.查看是否启动
					ps -ef | grep nginx
				10.
					快速停止   cd /usr/local/nginx/sbin && ./nginx -s stop
					完整停止	cd /usr/local/nginx/sbin && ./nginx -s quit
                    先停止再启动 ： ./nginx -s quit && ./nginx
                    重新加载配置文件 ./nginx -s reload
                11. cd /usr/local/nginx
                12.测试
                rm /usr/local/nginx/html/index.html
				echo "<?php phpinfo(); ?>" >> /usr/local/nginx/html/index.php
				echo "hello aqie" >> /usr/local/nginx/html/index.html

				13.问题：
					1.mkdir /var/run/nginx  重启虚拟机这个目录会被删除
					2.pid logs/nginx.pid;
						若是在nginx下创建logs目录，再把上面的注释去掉，或许也可以。


		2.安装mysql
			a. 查看电脑版本  uname -a
			b.	wget https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
				sudo rpm -Uvh mysql57-community-release-el7-11.noarch.rpm
				sudo yum install mysql-community-server
			c. 启动mysql  sudo service mysqld start
			   查看mysql服务状态 ： sudo service mysqld status
			d.  查看临时密码 ： cat /var/log/mysqld.log  | grep password  
				修改密码 ： SET PASSWORD FOR 'root'@'localhost' = PASSWORD('root'); 
							SET PASSWORD FOR 'root'@'localhost' = 'root'
				设置密码：
					1.set global validate_password_policy=0;
					2.set global validate_password_length=4;
					select @@validate_password_length;
				查看编码方式：show variables like 'character%';

				修改编码：vim /etc/my.cnf 
				[client]
				default-character-set=utf8
				[mysqld]
				character-set-server=utf8
			e.重启mysql服务
				systemctl restart mysqld.service

		3.编译安装php
			(https://secure.php.net/manual/zh/install.unix.nginx.php)
			(http://blog.csdn.net/abcdocker/article/details/55505076)
			1.下载
				wget -O php7.tar.gz http://cn2.php.net/get/php-7.0.4.tar.gz/from/this/mirror
			2. 解压 tar -xvf php7.tar.gz
			3. cd php-7.0.4
			4.安装依赖包
			yum install libxml2 libxml2-devel openssl openssl-devel bzip2 bzip2-devel libcurl libcurl-devel libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel gmp gmp-devel libmcrypt libmcrypt-devel readline readline-devel libxslt libxslt-devel
			5.配置文件
				1.libmcrypt源码安装方法
					http://ask.apelearn.com/question/7296
				2.vim /etc/ld.so.conf.d/local.conf
			6.make && make install
			7.配置环境变量
				vim /etc/profile
				末尾追加
				export PATH=/usr/local/php/bin:$PATH
				执行命令使改动生效
				source /etc/profile
			8.配置php-fpm 
				1.需要在安装软件包目录
				2.复制文件
					cp php.ini-production /etc/php.ini
					cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf
					cp /usr/local/php/etc/php-fpm.d/www.conf.default /usr/local/php/etc/php-fpm.d/www.conf
					cp sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm
					chmod +x /etc/init.d/php-fpm
				3.vim /usr/local/php/etc/php-fpm.d/www.conf
					user 和group改为 啊切
				4. nginx使用指定的用户.用户组运行
					vim /usr/local/nginx/conf/nginx.conf
					#即以web组的nginx用户来运行nginx.
					user nginx web;
					/usr/local/nginx/sbin/nginx -s reload
			9.nginx 解析php   站点根目录：/usr/local/nginx/html
				1.vim /usr/local/nginx/conf/nginx.conf   
				2. location ~ \.php$ {
				       root           /usr/local/nginx/html;
				       fastcgi_pass   127.0.0.1:9000;
				       fastcgi_index  index.php;
				       fastcgi_param SCRIPT_FILENAME /usr/local/nginx/html/$fastcgi_script_name;
				       include        fastcgi_params;
				    }
				3.重启nginx
					
		4.yum安装php
			1.安装epel-release
			rpm -ivh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
			2.rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
			3.yum install php70w

	2.配置nginx
		1.
	3.

三：
	1.关闭firewall：
		systemctl stop firewalld.service #停止firewall
		systemctl disable firewalld.service #禁止firewall开机启动
		firewall-cmd --state #查看默认防火墙状态（关闭后显示notrunning，开启后显示running）
	2、禁用/停止自带的firewalld服务
		#停止firewalld服务
		systemctl stop firewalld
		#禁用firewalld服务
		systemctl mask firewalld
	3.iptables防火墙
		a.  先检查是否安装了iptables
			service iptables status
		b.安装iptables
			yum install -y iptables
		c.安装iptables-services
			yum install iptables-services
		d.设置现有规则
			#查看iptables现有规则
			iptables -L -n
			#先允许所有,不然有可能会杯具
			iptables -P INPUT ACCEPT
			#清空所有默认规则
			iptables -F
			#清空所有自定义规则
			iptables -X
			#所有计数器归0
			iptables -Z
			#允许来自于lo接口的数据包(本地访问)
			iptables -A INPUT -i lo -j ACCEPT
			#开放22端口
			iptables -A INPUT -p tcp --dport 22 -j ACCEPT
			#开放21端口(FTP)
			iptables -A INPUT -p tcp --dport 21 -j ACCEPT
			#开放80端口(HTTP)
			iptables -A INPUT -p tcp --dport 80 -j ACCEPT
			#开放443端口(HTTPS)
			iptables -A INPUT -p tcp --dport 443 -j ACCEPT
			#允许ping
			iptables -A INPUT -p icmp --icmp-type 8 -j ACCEPT
			#允许接受本机请求之后的返回数据 RELATED,是为FTP设置的
			iptables -A INPUT -m state --state  RELATED,ESTABLISHED -j ACCEPT
			#其他入站一律丢弃
			iptables -P INPUT DROP
			#所有出站一律绿灯
			iptables -P OUTPUT ACCEPT
			#所有转发一律丢弃
			iptables -P FORWARD DROP
		e.其他规则设定
			#如果要添加内网ip信任（接受其所有TCP请求）
			iptables -A INPUT -p tcp -s 45.96.174.68 -j ACCEPT
			#过滤所有非以上规则的请求
			iptables -P INPUT DROP
			#要封停一个IP，使用下面这条命令：
			iptables -I INPUT -s ***.***.***.*** -j DROP
			#要解封一个IP，使用下面这条命令:
			iptables -D INPUT -s ***.***.***.*** -j DROP
		f.保存规则设定
			#保存上述规则
			service iptables save
		g.开启iptables服务 
			#注册iptables服务
			#相当于以前的chkconfig iptables on
			systemctl enable iptables.service
			#开启服务
			systemctl start iptables.service
			#查看状态
			systemctl status iptables.service
		h.查看已启动的服务列表：
			systemctl list-unit-files|grep enabled
		  查看服务是否开机启动：
		  	systemctl is-enabled iptables.service;echo $?
		i.映射端口（如将mysql默认的3306端口映射成1306对外提供服务）
			iptables -t mangle -I PREROUTING -p tcp --dport 1306 -j MARK --set-mark 883306 
			iptables -t nat -I PREROUTING -p tcp --dport 1306 -j REDIRECT --to-ports 3306 
			iptables -I INPUT -p tcp --dport 3306 -m mark --mark 883306 -j ACCEPT
	4.关闭防火墙
		永久性生效，重启后不会复原

		开启： chkconfig iptables on

		关闭： chkconfig iptables off
		即时生效，重启后复原

		开启： service iptables start

		关闭： service iptables stop
		查看防火墙状态： service iptables status
				  	 

四：
	./configure \
	--prefix=/usr/local/php \
	--with-config-file-path=/etc \
	--enable-fpm \
	--with-fpm-user=nginx  \
	--with-fpm-group=nginx \
	--enable-inline-optimization \
	--disable-debug \
	--disable-rpath \
	--enable-shared  \
	--enable-soap \
	--with-libxml-dir \
	--with-xmlrpc \
	--with-openssl \
	--with-mcrypt \
	--with-mhash \
	--with-pcre-regex \
	--with-sqlite3 \
	--with-zlib \
	--enable-bcmath \
	--with-iconv \
	--with-bz2 \
	--enable-calendar \
	--with-curl \
	--with-cdb \
	--enable-dom \
	--enable-exif \
	--enable-fileinfo \
	--enable-filter \
	--with-pcre-dir \
	--enable-ftp \
	--with-gd \
	--with-openssl-dir \
	--with-jpeg-dir \
	--with-png-dir \
	--with-zlib-dir  \
	--with-freetype-dir \
	--enable-gd-native-ttf \
	--enable-gd-jis-conv \
	--with-gettext \
	--with-gmp \
	--with-mhash \
	--enable-json \
	--enable-mbstring \
	--enable-mbregex \
	--enable-mbregex-backtrack \
	--with-libmbfl \
	--with-onig \
	--enable-pdo \
	--with-mysqli=mysqlnd \
	--with-pdo-mysql=mysqlnd \
	--with-zlib-dir \
	--with-pdo-sqlite \
	--with-readline \
	--enable-session \
	--enable-shmop \
	--enable-simplexml \
	--enable-sockets  \
	--enable-sysvmsg \
	--enable-sysvsem \
	--enable-sysvshm \
	--enable-wddx \
	--with-libxml-dir \
	--with-xsl \
	--enable-zip \
	--enable-mysqlnd-compression-support \
	--with-pear \
	--enable-opcache