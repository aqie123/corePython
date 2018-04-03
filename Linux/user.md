一：查看当前用户 whoami
	1. 添加用户 useradd aqie
	2. 设置密码 passwd  aqie
	3. ssh 登录 ssh aqie@140.143.238.151
	4. 删除用户 userdel aqie
二： 创建组
	1. ll 查看文件用户权限 及用户组
		权限 文件拥有者 用户组
	2. 创建组 groupadd groupName
	   查看组	cat /etc/group
	   删除组 groupdel groupName
	   查看所有组名 groupmod
	   修改文件所属组 chgrp yyy 1.py
	   修改文件所属人 chown yyy 1.py
	   查看所有用户 cat /etc/passwd | cut -f 1 -d
	   创建用户xxx 到组yyy   adduser xxx -g yyy
	3. ll  r=4 w=2 x=1
	 d代表文件夹 文件所有者权限 同组者权限 其他用户权限 硬连接数 文件所属人
	 文件所属组 文件大小 创建日期
	 1.修改文件所有者权限 chmod u=rwx 1.py
	 2.修改文件同组者权限 chmod g=rwx 1.py
	 3.修改文件对其他人权限 chomd o=rwx 1.py
