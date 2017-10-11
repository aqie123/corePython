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
					启动       cd /usr/local/nginx/sbin/ && ./nginx
					快速停止   cd /usr/local/nginx/sbin && ./nginx -s stop
					完整停止	cd /usr/local/nginx/sbin && ./nginx -s quit
                    先停止再启动 ： ./nginx -s quit && ./nginx
                    重新加载配置文件 ./nginx -s reload
                11. cd /usr/local/nginx
                12.测试
                rm /usr/local/nginx/html/index.html
				echo "<?php phpinfo(); ?>" >> /usr/local/nginx/html/index.php
				
				echo "hello aqie" >> /usr/local/nginx/html/index.html

				13.启动问题：
					1.mkdir /var/run/nginx  重启虚拟机这个目录会被删除
					2.pid logs/nginx.pid;
						若是在nginx下创建logs目录，再把上面的注释去掉，或许也可以。
					3./usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf 
				14. html正常显示,php 404
					1.php-fpm没有运行



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
			f.mysql 允许远程用户登录访问
				1.GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '753951kzlAqie*7jskols' WITH GRANT OPTION;
				2.FLUSH PRIVILEGES; 

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

					启动php-fpm
					/etc/init.d/php-fpm start
					service php-fpm restart  重启
				3.vim /usr/local/php/etc/php-fpm.d/www.conf
					user 和group改为 啊切
				4. nginx使用指定的用户.用户组运行(这个没试过)
					vim /usr/local/nginx/conf/nginx.conf
					#即以web组的nginx用户来运行nginx.
					user nginx web;
					/usr/local/nginx/sbin/nginx -s reload
				5 启动

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
					cd /usr/local/nginx/sbin
					./nginx -s quit && ./nginx
			10. 配置php.ini (/etc/php.ini)  （/usr/local/php/etc/php-fpm.d/www.conf）
				1. 报错 display_errors = On  vim /usr/local/php/etc/php-fpm.d/www.conf  php_flag[display_errors] = on
				2.
					
		4.yum安装php
			1.安装epel-release
			rpm -ivh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
			2.rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
			3.yum install php70w



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
			iptables -I INPUT -p tcp --dport 80 -j ACCEPT

			#开放443端口(HTTPS)
			iptables -A INPUT -p tcp --dport 443 -j ACCEPT
			
			# 关闭8002端口
			iptables -I INPUT -p tcp --dport 8002 -j DROP

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

			开放Telnet端口
			iptables -A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 23 -j ACCEPT
		e.其他规则设定
			#如果要添加内网ip信任（接受其所有TCP请求）
			iptables -A INPUT -p tcp -s 45.96.174.68 -j ACCEPT
			iptables -A INPUT -s 192.168.0.135 -j ACCEPT
			#过滤所有非以上规则的请求
			iptables -P INPUT DROP
			#要封停一个IP，使用下面这条命令：
			iptables -I INPUT -s ***.***.***.*** -j DROP
			#要解封一个IP，使用下面这条命令:
			iptables -D INPUT -s ***.***.***.*** -j DROP

			iptables -A INPUT -s 192.168.0.0/24 -j ACCEPT
		    //允许源IP地址为192.168.0.0/24网段的包流进（包括所有的协议，这里也可以指定单个IP）
		    iptables -A INPUT -d 192.168.0.22 -j ACCEPT
		    //允许所有的IP到192.168.0.22的访问
		    iptables -A INPUT -p tcp --dport 80 -j ACCEPT 
		    //开放本机80端口
		    iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
		    //开放本机的ICMP协议
		f.保存规则设定
			#保存上述规则
			service iptables save

			 删除规则
			 iptables -D INPUT -s 192.168.0.21 -j ACCEPT
			 保存规则
			 service iptables save
			 清空缓冲区
			 iptables -F
			 重启
			 service iptables restart
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
		j.查看端口情况
			1.netstat -an | grep 22
			2.关闭端口号:iptables -A INPUT -p tcp --drop 端口号-j DROP
 
                 iptables -A OUTPUT -p tcp --dport 端口号-j DROP
 
			 打开端口号：iptables -A INPUT -ptcp --dport  端口号-j ACCEPT
			3.lsof -i:80  查看端口情况
			4，终极大法
				  iptables -F
				  iptables -P INPUT ACCEPT
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


五： linux 基本使用
	1.中文输入法
		a. super + 空格
	2.创建文件夹快捷方式
		1.ln -s /home/LXBC /etc/LXBC553(快捷方式)
			ln -s /usr/local/nginx/html(源文件) /home/aqie/桌面/html
	3.修改文件夹权限
		1.chmod -R  777  /usr/local/nginx/html
		2.chmod -R  777  /home/aqie
	4.创建用户和组(todo)
	5.下载git项目 test
		1.测试pdo连接数据库，并在浏览器输出
	6.修改vim tab空格
		1.vim ~/.vimrc
		2. vim /etc/vimrc
	7.  文件操作
		a. /home/work下的文件复制到/home/temp里面？
			cp -R /home/work/* /home/temp
			cp /home/aqie/aqie/test/mypdo.php  /usr/local/nginx/html
		b.在nginx/html 里创建home/aqie/aqie 软连接
			ln -s /home/aqie/aqie /usr/local/nginx/html/aqie

		c. 删除文件(问题：删除软连接里面的文件，源文件会不会消失) 会消失
			/home/aqie/aqie/test/README.md  真实的
			rm /usr/local/nginx/html/aqie/test/README.md  删除这个上面也没了
			测试：删除软连接
			rm -rf /usr/local/nginx/html/aqie
			源文件不会受影响

			做软连接： 源文件-> /home/aqie/aqie/test
					   映射->   ln -s /home/aqie/aqie  /usr/local/nginx/html
			删除 rm -rf /usr/local/nginx/html
			通过软连接显示文件：
			echo "<?php echo "hello aqie"; ?>" >> /home/aqie/aqie/test.php
			echo "粗错啦！！！" >> /home/aqie/aqie/50x.html

	8.vim常见操作
		1.快速查找
			/error_reporting = E_ALL
		2.  
			全部删除：按esc后，然后dG
			全部复制：按esc后，然后ggyG
		3.撤销
			u   撤销上一步的操作
			Ctrl+r 恢复上一步被撤销的操作
		4.G: 移动到文档末尾
		  gg: 移动到文档开头
		5.dd：剪切当前行
		6.跳转到行尾 End
		7.格式化代码
			a. gg跳转到第一行
			b. shift + v转到可视模式
			c. shift + g 全选
			d. =
		    格式化全文： gg=G
		8. vim 插件 Vundle （）
			1.git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
			2. 配置文件  vim /home/aqie/.vimrc
				a.tree :helptags ~/.vim/bundle/nerdtree/doc/
				b.ctrl + w 切换
				c. t 在新标签页打开
		9.升级 vim8 (http://blog.csdn.net/u013388603/article/details/72780586)
			1. 
				cd /usr/local/src git clone git@github.com:vim/vim.git
				cd vim
				cd /usr/local/src/vim/src

				./configure --prefix=/usr/local/vim8
				make && make install
			2.编辑这个文件  /usr/local/vim8/bin/vim /etc/profile.d/path.sh
			 添加  export PATH=$PATH:/usr/local/vim8/bin/
			 使命令生效  source /etc/profile.d/path.sh
			3. ./configure --prefix=/usr/local/vim8 --enable-pythoninterp=yes --enable-python3interp=yes --with-python-config-dir=/usr/bin/python2.7-config --enable-multibyte 

			./configure --with-features=huge --enable-multibyte --enable-rubyinterp=yes --enable-pythoninterp=yes --with-python-config-dir=/usr/bin/python2.7-config --enable-python3interp=yes --with-python3-config-dir=/usr/local/bin/python3.5-config  --enable-gui=gtk2 --enable-cscope --prefix=/usr/local/vim8
			4. vim --version  查看是否支持python
		10.
			系统 vimrc 文件: "$VIM/vimrc"
		     用户 vimrc 文件: "$HOME/.vimrc"
		   第二用户 vimrc 文件: "~/.vim/vimrc"
		11. vim 配置
			1.http://blog.csdn.net/g_brightboy/article/details/14229139
			2.插件安装： http://blog.csdn.net/namecyf/article/details/7787479
		12.复制 粘贴 剪切 删除
			1. 2yy拷贝当前行及其下一行
			2. shift+p 在当前行前粘贴
			3. :1,10d 将1-10行剪切。
			4. 
				a.删除不能用 : set backspace=indent,eol,start
				b.3dd代表删除三行
				c.用v选中文本之后可以按y进行复制，如果按d就表示剪切，之后按p进行粘贴
			5.跳转到指定行
				a. :12跳转到第十二行
				b. dw 删除光标后单词剩余部分
				c. d$ 删除光标之后该行剩余部分
				d. dd 删除当前该行
				e. :1 :$ 跳转到行首行尾  gg跳转到首行，G跳转到最后一行
					下一行o 
				f.跳转到光标之前位置 Ctrl + O
		13.分屏
			1.vim -o 
			2.vim -On file1 file2 ...
		14. 代码折叠
			zc 折叠最外层
			zo 展开最外层
			za 互相切换
		15.撤销
			1. u 撤销
			2. ctrl+r 反撤销
		16.展示目录
			1. tree vendor -L 2 行级限制
		17.vim多行缩进
			1.v进入visual状态，选择多行，用>或<缩进或缩出 
			2.多行用n== ; gg=G可对整篇代码进行排版
			3. gg   shift+G 首尾
			4. (http://blog.csdn.net/topasstem8/article/details/6678215)

	9. linux 连接github
		1.git config --global user.email "2924811900@qq.com"
  		  git config --global user.name "aqie123"
  		2.生成密钥
  			a.ssh-keygen -t rsa -C "2924811900@qq.com"
  			b. cd /home/aqie/.ssh/id_rsa
  			c.cp /home/aqie/.ssh/id_rsa.pub .
  			d. 验证
  				ssh git@github.com

  	


六。linux 下编译安装yaf
	1.git clone https://github.com/laruence/php-yaf.git
	2.cd php-yaf
	3.git branch -a
	3.5. yum install m4
		 yum install autoconf

	#开始编译安装
	4.  /usr/local/php/bin/phpize
		会新建一个configure文件
	5. ./configure --with-php-config=/usr/local/php/bin/php-config
	6.make && make install
		解析makefile内容
		find ./ -name 'yaf.so'
	7.vim /etc/php.ini 
	8.extension = 安装完成显示的目录地址/yaf.so
	9. extension =/usr/local/php/lib/php/extensions/no-debug-non-zts-20151012/yaf.so
		ls modules/
	10.notes
		which php   /usr/local/php/bin/php
		find / -name 'php-config'     /usr/local/php/bin/php-config
		netstat -tpnlu
		ifconfig -a   查看本机ip
	11.下载 yaf
		1. cd /home/aqie/phpApi  （https://github.com/laruence/yaf）
		2. cd yaf/tools/cg
		3. ./yaf_cg phpapi
		4. cd output 
		5. yum -y install tree tree phpapi/
		6. cp -rf phpapi/*  /home/aqie/phpApi/
		7. 删除文件夹  rm -rf yaf/



七。配置nginx 多站点
	1.nginx 配置文件在 vim /usr/local/nginx/conf/nginx.conf
		cd /usr/local/nginx/conf
		include vhosts/*.conf;
		mkdir vhosts
		http{}最后添加 include vhosts/*.conf;
	2.  配置 vim /usr/local/nginx/conf/vhosts/www.phpapi.com.conf
		/usr/local/nginx/sbin/nginx -t    检测配置文件正确性 
		mkdir /home/aqie/phpApi; 项目根目录
		vim /home/aqie/phpApi/index.html  成功
		vim /home/aqie/phpApi/test.php
		location / {
            root  /home/aqie/phpApi;
            index  index.php index.html index.htm;
        }
        
        location ~ \.php$ {
             root           /home/aqie/phpApi;
             fastcgi_pass   127.0.0.1:9000;
             fastcgi_index  index.php;
             fastcgi_param  SCRIPT_FILENAME  /home/aqie/phpApi$fastcgi_script_name;
             include        fastcgi_params;
        }
        if (!-e $request_filename) {
    		rewrite ^/(.*)  /index.php?$1 last;
  		}
  	3.  问题： nginx: [error] open() "/var/run/nginx/nginx.pid" 
  		/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf

八。
	1.编写phpApi (cd /home/aqie/phpApi)
		a. mv /usr/local/nginx/html/phpApi/README.md .
	2.自定义路由
		$route = new Yaf_Route_Rewrite(
     　　'product/:ident',
     　　array(
     　　　　'controller' => 'products',
     　　　　'action' => 'view'
     　　)
     	);
     	$router->addRoute('product', $route);
    3. 网站根目录 ：cd /home/aqie/phpApi  修改权限: chmod -R  777 /home/aqie/
    4. cp Index.php User.php  复制一个控制器
    	user/reg/:username -> 访问User控制器下面的reg方法 (http://www.phpapi.com/user/reg)


九，centos 编译安装python3.5
	1.wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz
	2.tar -zxvf Python-3.5.1.tgz
	3.mv Python-3.5.1 /usr/local
	4.ll
	5.  查看python依赖
		ll /usr/bin | grep python
	6.rm -rf /usr/bin/python
	7.cd /usr/local/Python-3.5.1/
	8. ./configure
	9.make && make install
	10.ln -s /usr/local/bin/python3.5 /usr/bin/python
	11.  find / -name python2.7-config
	12. /usr/bin/python2.7-config   /usr/local/bin/python3.5-config

	13.修改默认为python2
		1. rm /usr/bin/python
		2. ln -s /usr/bin/python2 /usr/bin/python


十。php定时执行任务
	1.  开始–》附件–》系统工具–》任务计划程序 
		"D:\phpStudy\php\php-5.6.27-nts\php.exe" -q "D:\test\test.php"
		"E:\phpStudy\php\php-5.5.38\php.exe" -q "E:\test\test.php"
	2.curl http://60.205.217.197:81/crowd/go/index/hello
	3.curl http://60.205.217.197:81/crowd/go/index/aqie

十一。curl配置
	1. CURL_HOME   "%CURL_HOME%";

十二：mysql 触发器
	1. 向 auth_admin 表写入同时向admin插入数据
		a.创建触发器
			DELIMITER \\\
			create trigger goods_attach after insert on ecs_goods for each row
			begin
				set @v1 = new.goods_id;
				insert into ecs_goods_attach(goods_id) values(@v1);
			end \\\
			DELIMITER ;

			测试： insert into auth_admin(admin_name,password) values('aqie','123');
		b.SHOW TRIGGERS;
		c.删除 DROP TRIGGER [IF EXISTS] goods_attach
	2. 从一张表读取数据写入另一张表
		insert into ecs_goods_attachs(goods_id) select goods_id from ecs_goods order by goods_id;
	3. 创建一张结构类似表
		create table ecs_goods_attachs like ecs_goods_attach;


十三：xshell 连接虚拟机
	1. 192.168.41.128(虚拟机)
	2. 192.168.0.135(本机)
	3. iptables -A INPUT -p tcp -s 192.168.0.135 -j ACCEPT
	4. /home/aqie/phpApi  yaf 项目
	   /home/aqie/aqie    本地测试项目
	   nginx 根目录 ： /usr/localnginx/html

	   a.先删除之前软连接 rm -rf /usr/local/nginx/html
	   b.创建软连接  ln -s /home/aqie/phpApi /usr/local/nginx/html
	   c.添加规则
	   		1.vim /usr/local/nginx/conf/nginx.conf
	   		2.vim /usr/local/nginx/conf/vhosts/www.phpapi.com.conf

十四：线缆被拔出
	1. 控制面板->管理工具->服务

十五：yaf框架基本使用
	1. 路由
		a. ?c=index&a=test
		b. 
	2.
		public $errno = 0;
		public $errmsg = '';
		private $_db;
		public function __construct() {
			$this->_db = new PDO('mysql:host=127.0.0.1;dbname=test;','root','root');
	    }
	    $arr2 = $res->fetch(PDO::FETCH_ASSOC );     //关联
十六：文件操作
	1. 查看文件权限(创建者拥有权限,与拥有着同组用户拥有权限,其他用户拥有的权限)
		a”表示所有用户，“u”表示创建者、“g”表示创建者同组用户、“o”表示其他用户；“+”表示添加权限，“-”表示取消权限；“r”表示读权限、“w”表示写权限、“x”表示写权限。
		ls -l
	2. 修改文件权限
		chmod -R 777 /phpApi
		给文件夹下面所有文件添加执行权限
	3.  解压
		unzip php.zip
	4.文件移动
		cp -rf WxpayAPI_php_v3.0.1/lib ../ThirdParty/Wxpay
		cp -rf ../tmp/WxpayAPI_php_v3.0.1/example/phpqrcode ./Qrcode
十七：centos
	1. http://rasilient.com
十八： Vim进阶操作
	a.  格式化显示代码
		1，gg 跳转到第一行
		2，shift+v 转到可视模式
		3，shift+g 全选
		4，按下神奇的 =
		5. 快速格式化 gg=G
	b. 分屏
		1.vim -O User.php ../../models/User.php
		2.分屏切换 ctrl + w
	c.查看 grep 'errmsg' ./ -r
	d.vim指定替换多行文本
		以下命令将文中所有的字符串idiots替换成managers：
		:1,$s/idiots/manages/g
		通常我们会在命令中使用%指代整个文件做为替换范围：
		:%s/search/replace/g
		以下命令指定只在第5至第15行间进行替换:
		:5,15s/dog/cat/g
		以下命令指定只在当前行至文件结尾间进行替换:
		:.,$s/dog/cat/g
		以下命令指定只在后续9行内进行替换:
		:.,.+8s/dog/cat/g
		你还可以将特定字符做为替换范围。比如，将SQL语句从FROM至分号部分中的所有等号（=）替换为不等号（<>）：
		:/FROM/,/;/s/=/<>/g
	e.ctrl+shift+F
	f.多行缩进
		1.v
		2.nj
		3.><
	g. 新建文件
		1. :new文件名
		2. :e 打开文件
		3. :x 退出，文件更改则保存
		4. ! 可以使用 shell
		5. :open
		6. :bn 下一个文件 :bp 下一个文件
	h.全选删除
		1. ggdG   :%d
	i.复制保留原格式
		1. :set paste  开启
		2. :set nopaste  关闭
		3. :h paste 查看状态
	j. 配置所有
		1. vim   /etc/vimrc 
十九：
	1.linux基本操作
		1.tail -f nginx.log  查看日志
		2.  进入nginx配置目录 cd /usr/local/nginx/conf/
			grep 'log_format' ./ -r
		3. nginx 日志目录 cd /var/log/nginx
		4.rz 上传文件到linux
		5. find /home/aqie -name run.php
			find ./  当前目录 
二十：安装redis
	1. wget http://download.redis.io/releases/redis-4.0.2.tar.gz
	2.tar zxvf  解压
	3. make install
	4. which redis-check-rdb    /usr/local/bin/redis-check-rdb
	5. 启动redis  redis-server
	6. 查看启动服务： netstat -tpnlu
	7.vim redis.conf
	8.redis-server ./redis.conf          /usr/local/bin/redis-cli
	9. ps -ef | grep redis
	10.配置文件 ： redis-server /home/aqie/redis-4.0.0/redis.conf
	11. 关闭redis redis-cli shutdown
	12. 安装php  redis扩展  ./composer.phar require predis/predis
二十一：常用php插件
	1. https://packagist.org/
	2. pecl.php.net   php官网
	3. reids 官网
二十二： CentOS 安装 supervisor 进程管理工具
	1.yum install python-setuptools
		a.安装pip （https://pypi.python.org/pypi/pip）
			1.wget https://bootstrap.pypa.io/get-pip.py
			2.python get-pip.py
	2.pip install supervisor
	3. ps aux | grep superv      supervisord
	4. 生成supervisord配置文件
		echo_supervisord_conf > /usr/supervisord.conf
		supervisord -c /usr/supervisord.conf
	5.supervisorctl -h
	6.查看配置 vim /usr/supervisord.conf (改末尾include)
		创建目录 mkdir /usr/supervisord
	7.cd /usr/supervisord    vim nginx.ini
	8. supervisorctl reload
	9. supervisorctl status
	10. supervisorctl start nginx
	11. supervisorctl stop all
	12. ps aux | grep nginx  查看nginx状态
		killall nginx
		ps aux | grep nginx
		supervisorctl status
	13. supervisorctl reload
		1. supervisorctl status
		2. ps aux | grep nginx   没有nginx进程
		3.supervisorctl start nginx  启动nginx
	14.改成redis  
		(http://blog.csdn.net/albertfly/article/details/51581368 redis配置)
		(http://www.jb51.net/article/101508.htm)
		1. cp nginx.ini redis.ini
		2. ps aux | grep redis
		3. redis 退出 redis-cli shutdown
		4.which redis-server    /usr/local/bin/redis-server
		5. vim redis.ini
		6. supervisorctl reload
		7. supervisorctl status
		8. ps aux | grep redis  没有运行
		9. supervisorctl start redis  启动redis
		10.  supervisorctl status  多点几下
二十三：安装Telnet服务
	1. 查看linux版本 cat /etc/issue
	2. rpm -qa | grep telnet  （rpm -qa xinetd  rpm -qa telnet-server）
		yum list |grep telnet
		yum list |grep xinetd
		yum install xinetd.x86_64
	3.  xinetd服务加入开机自启动
		systemctl enable xinetd.service
	4.  开机启动
		systemctl enable telnet.socket
	5.  systemctl start telnet.socket
		systemctl start xinetd
	3. yum install telnet-server 
	4. 开启 ：
		a. 编辑/etc/xinetd.d/telnet, 将其中的 disable = yes 的yes改为no
		b. chkconfig telnet on
	5. telnet 192.168.41.128 886
	6. Ctrl + ] 会呼出telnet的命令行
二十四：调试错误
	3.strace php test.php，或者strace -p 进程ID
	4.使用tcpdump工具分析网络通信过程
	5.统计函数调用的耗时和成功率
		使用xhporf/xdebug导出PHP请求的调用过程，然后分析每个函数调用的过程和耗时。
		如mysql查询，curl，其他API调用等，通过记录起始和结束时microtime，返回的是不是false， 可以得到调用是否成功，耗时多少
	6.  gdb使用
		gdb -p 进程ID，再配合php-src的.gdbinit zbacktrace等工具，可以很方便地跟踪PHP程序的执行
	7.  查看PHP内核和扩展源码
二十五：PHP 中 9 大缓存技术总结(http://developer.51cto.com/art/201509/491334.htm)
	1. 全页面静态化缓存
		Ob_start()
		$content = Ob_get_contents();
		Ob_end_clean();
	2. 页面部分缓存
		1.ob_get_contents 
		2.ESI之类的页面片段缓存策略
	3.数据缓存
		1.其实缓存文件中缓存的就是一个php数组之类；
	4.查询缓存
		1.就是根据查询语句来缓存；将查询得到的数据缓存在一个文件中，下次遇到相同的查询时，就直接先从这个文件里面调数据，不会再去查数据库；但此处的缓存文件名可能就需要以查询语句为基点来建立唯一标示
	5. 按内容变更进行缓存
		1.一个人流量很大的商城，商品很多，商品表必然比较大，这表的压力也比较重；我们就可以对商品显示页进行页面缓存
		2.当商家在后台修改这个商品的信息时，点击保存，我们同时就更新缓存文件；那么，买家访问这个商品信息时，实际上访问的是一个静态页面，而不需要再去访问数据库；
	6.内存式缓存(memcached是高性能的分布式内存缓存服务器。)
		1.将需要缓存的信息，缓存到系统内存中，需要获取信息时，直接到内存中取
	7.apache缓存模块
		1,安装apache时：./configure –enable-cache –enable-disk-cache –enable-mem-cache
	8. php APC缓存扩展
		1.
	9.Opcode缓存 （XCache、Turck MM Cache、PHP Accelerator）
		1.首先php代码被解析为Tokens，然后再编译为Opcode码，最后执行Opcode码，返回结果；所以，对于相同的php文件，第一次运行时 可以缓存其Opcode码，下次再执行这个页面时，直接会去找到缓存下的opcode码，直接执行最后一步
二十六：swoole学习 (swoole是一个高性能的异步网络通信引擎，为php提供了多线程功能)
	1.php不支持多线程
	2.查看gcc版本 gcc -v 
	3. wget https://github.com/swoole/swoole-src/archive/v1.9.21.tar.gz
	4.tar zxvf v1.9.21.tar.gz
	5. cd swoole-src-1.9.21
	6. phpize 
	7. ./configure
	8. make  && make install 
	9. 安装位置  /usr/local/php/lib/php/extensions/no-debug-non-zts-20151012/
	/usr/local/php/include/php/
	10. vim /etc/php.ini
	11. extension=/usr/local/php/lib/php/extensions/no-debug-non-zts-20151012/swoole.so
	12. cd /usr/local/nginx/sbin && ./nginx -s stop && ./nginx   service php-fpm restart
	13. 
		1. cp /usr/local/php/lib/php/extensions/no-debug-non-zts-20151012/swoole.so /usr/local/php/include/php/
		2. extension_dir = “/usr/local/web/php/lib/php/extension/” 
		3. extension=curl.so 
二十七：
	1.ip addr
二十八：Swoole使用
	1. php run.php -c 100 -n 10000 -s tcp://192.168.41.128:886 -f long_tcp
	2. 
二十九：安装mariadb
	1. yum install mariadb-server mariadb
	2. yum install php php-fpm php-mysql
	3. 启动 systemctl start mariadb
			systemctl status mariadb
