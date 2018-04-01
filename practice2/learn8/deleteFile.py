import os
import fnmatch


"""
import shutil  
# 目录data下的train及其下的所有文件,linux中的rm -rf
shutil.rmtree('data/train') 

# 递归的创建目录data/train，相当于Linux中的 mkdir -p
os.makedirs('data/train')  
"""
# 递归删除文件
def search(pattern, root = os.curdir):
	for path, dirs, files in os.walk:
		"""
		三元tupple(dirpath, dirnames, filenames),
		起始路径string,
		dirpath下所有子目录的名字,list
		包含了非目录文件的名字,list
		"""
		for filename in fnmatch.filter(files,pattern):
			yield os.path.join(path, filename)


mypath = os.path.abspath('.')
filesearch = search(mypath)
print(next(filesearch))
"""
for x in filesearch:
	print("Deleting %s" % x)
	# os.remove(x)
"""