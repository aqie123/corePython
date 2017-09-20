1.chmod a+w -R /home/PycharmProjects/       ./vmware-install.pl
2.su root
3.yum -y install kernel-devel-$(uname -r)
4.yum install gcc gcc-c++ kernel-devel
5.查看可以登录系统的用户：cat /etc/passwd | grep -v /sbin/nologin | cut -d : -f 1
  查看系统中有哪些用户：cut -d : -f 1 /etc/passwd
6.userdel -rf name  删除用户
7.rm -rf  /home/git 删除目录
    rm   /home/git/.ssh   删除文件

