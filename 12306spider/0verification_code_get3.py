#coding:utf-8

import requests
from PIL import Image
import pytesseract
from numpy import *
import matplotlib.image as mpimg

#获取12306票价查询验证码
url='https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=other&rand=sjrand'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
req=requests.get(url=url,headers=headers,verify=False)
with open('img/code.jpg','wb') as f:
    f.write(req.content)

#分析验证码图片获取字符串

image = Image.open('img/code.jpg')
# 图片转换为像素
image.load()

#把彩色图像转化为灰度图像
img_g = image.convert('L')
img_g.save('img/codeg.jpg')

#PIL Image图片转换为numpy数组
im_array =array(img_g)
print im_array

#4、将 numpy 数组转换为 PIL 图片
#这里采用 matplotlib.image 读入图片数组，注意这里读入的数组是  float32 型的，
# 范围是 0-1，而 PIL.Image 数据是 uinit8 型的，范围是0-255，所以要进行转换：
#
# lena =mpimg.imread('lena.png') # 这里读入的数据是 float32 型的，范围是0-1
# im = Image.fromarray(np.uinit8(lena*255))


print pytesseract.image_to_string(img_g)


