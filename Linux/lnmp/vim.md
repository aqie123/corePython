a. vim advanced
	1. set clipboard=unnamed
	2.Vundle （https://github.com/VundleVim/Vundle.vim）
		1.http://blog.csdn.net/g_brightboy/article/details/14229139
		2.插件安装： http://blog.csdn.net/namecyf/article/details/7787479
	3. vim ~/.vimrc   vim /etc/vimrc
b.vim base
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
3.settings
  set clipboard=unnamed
  syntax on
  set backspace=indent,eol,start
  set tabstop=4
  set softtabstop=4
  set shiftwidth=4
  set noexpandtab
  set number
  set autoindent
  set cindent