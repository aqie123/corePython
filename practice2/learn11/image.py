from PIL import Image,ImageFilter
im = Image.open('../aqie.jpg')
# 获得图片尺寸
w,h = im.size
print("Original image size : %sx%s" %(w, h))

# 缩放到50%
'''
im.thumbnail((w/2, h/2))
im.save('thumb-aqie.jpg', 'jpeg')
'''

# 切片、旋转、滤镜、输出文字、调色板等一应俱全

# 模糊效果
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur-aqie.jpg', 'jpeg')