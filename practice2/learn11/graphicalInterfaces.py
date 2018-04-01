# 图形界面
# 第三方库： Tkinter wxWidgets Qt GTK

from tkinter import *
# 第一步; 从Frame派生一个Application类，这是所有Widget的父容器：

class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self, text = "Hello Aqie")
		self.helloLabel.pack()
		self.quitButton =Button(self, text = 'Quit', command = self.quit)
		self.quitButton.pack()

# 在GUI中，每个Button、Label、输入框等，都是一个Widget
# Frame则是可以容纳其他Widget的Widget，
# 所有的Widget组合起来就是一棵树。

# pack()方法把Widget加入到父容器中，并实现布局。
# pack()是最简单的布局，grid()可以实现		

# 第二步： 例化Application，并启动消息循环
app = Application()
# 设置窗口标题
app.master.title('Hello  aqie')
# 主消息循环
app.mainloop()