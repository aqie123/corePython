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
	16.

二：
	1.配置lnmp
		1.安装nginx

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


		3.安装php
	2.配置nginx
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
				  	 