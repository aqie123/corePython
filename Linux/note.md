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

