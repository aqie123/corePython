### 文件常用操作
	1. touch a.txt 新建文件
	2. ls -l 列出文件夹下文件的权限
	3. ls -a -l -h 查看隐藏文件
	4. ls --help 查看帮助 man ls
	5. 查看文件 cat / more
	6. 查看文件重定向 ls -alh /bin >> temp/bin.txt
	   ls -alh /bin | more  按f往下走
	7. mkdir 创建文件夹
	   rmdir 删除文件夹,只能删除空文件夹
	8. 软连接 ln -s 1.txt 1-softlink.txt
	  硬连接 ln 1.txt 1-hardlink.txt
	  当一个文件的硬连接数为0,数据被删除
	9. 文件搜索  文件内容
		1.grep "创建" Linux/file.md
		2.grep -v "ntfs" a.txt  不包含
		3.grep "^ls" Linux/file.md
	10. find 查找文件 文件名
		1.find ./ -name test.sh
		2.find ./ -name ’*.sh‘
		3.find /tmp -size +2M
		4.find /tmp -size +4M -size -5M
		5.find /tmp -perm 777 查找777权限的文件
	11. tar
		-c:生成档案文件,创建打包文件
		-v:列出归档解档进度
		-x:解开档案文件
		-z：
		-f:指定档案文件名称,必须放最后
		-t:列出档案包中文件
	12. 文件中查找
		1. /name 查找
		2. n 查看下一个匹配
### 
