 # -*- coding: utf-8 -*-

from PIL import Image
import pytesseract
import sys

#简单图片识别方法
# image = Image.open(sys.argv[1])  #m命令行中读取文件

image = Image.open('img/7364.jpg')

# 图片转换为像素
image.load()

#把彩色图像转化为灰度图像
img_g = image.convert('L')
img_g.save('img/7365g.jpg')

print pytesseract.image_to_string(img_g)

