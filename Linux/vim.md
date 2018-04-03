一：vim 文件夹操作
	建立文件夹 ： !mkdir corePython/vim
	建立文件  ： sp vim/note.md
二：基本操作
	1. yy 复制当前行
	2。 p 粘贴
	3. dd 删除一行  
		D:删除光标后面  
		u:撤销操作  
		ctrl+r:反撤销
		d0 : 删除光标前面的 
		x: 单个字母删除 先删除当前再删除右边
		X: 向左单独删除
	4. 复制多行 2yy p
	5. 剪切 4dd
	6. hjkl  
		h:向左
		l:向右
		j:向下
		k:向上
	7. 快速定位
	   M : 当前屏幕中间
	   L : 最后一行
	   H : 第一行
	   Ctrl + f 向下翻页
	   ctrl + d 向下翻半页	

	   ctrl + b 向上翻页
	   ctrl + u 向上翻半页

	   快速定位到行 30G
	   快速定位到行尾 G
	   快速定位到行首 gg
	8. 编辑下一行 o
	   快速编辑上一行 O
	9. w : 以单词向后进行划分
	   b : 以单词向前进行划分
	10. v 选中 > 向右移， < 向左移	
		V 选中 然后 . 重复执行	
    11. r : 替换
	    R : 替换光标以及后面的字符
	12. i 插入
		I 插入行首
		a: 插入光标后一个字符
		A:插入行末
		{:按段移动
	13. 查找hello ： /hello
		全文替换 hello 变成world  : %s/hello/world/g
	14. 121,128s/world/hello/g
三：

四：
	
