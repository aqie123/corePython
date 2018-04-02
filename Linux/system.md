一：系统管理
	1.查看日历 cal
		cal -y 2018 查看 2018 年日历
		查看日期 date
		指定格式 date "+%Y-%m-%d"
	2.查看当前终端下进程 ps
	  查看所有进程 ps -aux 
	  永远显示电脑运行情况 top
	3.杀死进程 kill -9 9822
	4.重启 reboot
		init 0 关机
		init 6 重启
	  shutdown -h 20:00
	  shutdown -h +10  十分钟后关机
	5.检测磁盘空间
		df 硬盘使用情况
		df -h  显示大小
		du -h  显示当前路径文件占用
	6.查看本地连接
		ifconfig
