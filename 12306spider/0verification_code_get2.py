#coding:utf-8

from PIL import Image
import pytesseract

def  imgprocess(name):

    #打开图片
    im = Image.open(name)

    #灰度化
    img_g = im.convert('L')
    img_g.save('img/1g.jpg')

    #二值化,二值图:0表示黑色,1表示白色
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    img_b = img_g.point(table, '1')
    img_b.save('img/1b.jpg')
    #识别
    strings = pytesseract.image_to_string(img_b)
    return strings

imgprocess('img/2.jpg')
