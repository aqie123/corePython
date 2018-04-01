# 图片缩略图
from PIL import Image
im = Image.open("aqie.jpg")

im.thumbnail((200,200)
im.save('thumb.jpg', 'JPEG')