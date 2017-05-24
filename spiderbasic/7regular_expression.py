# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境

import re

#demo1
# def re_demo():
#     #解析价格
#     txt = "if you purchase more than 100 sets, the price of product a is $9.9"
#     m = re.search(r"(\d+).*\$(\d+\.?\d*)", txt)
#     print (m.groups())
# if __name__ == "__main__":
#     re_demo()

def re_method():
    str='this is a apple.its price is $4.6'

    # print (re.findall(r"\d+\.?\d*",str))

    # #finditer
    # r = re.finditer(r"\d+\.?\d*", str)
    # for m in r:
    #     print (m.group())

    # #sub 替换
    # print (re.sub(r"\d+\.?\d*", "4000" ,str))

    # #group 组的元素
    # m = re.match(r'(\w+) (\w+)',str)
    # print (m.group(0, 1, 2))
    # print (m.groups(0))


    # print (re.search(r'(\d)(\d)(\d)\1\2\3','135135').groups())
    # print (re.search(r'(\d{3})\1', '135135').groups())

    str2 = 'the number is 20.5'
    r = re.compile(r'''
                    \d+  #整数部分
                    \.?  #小数点，可能包含也不可能包含
                    \d*  #小数部分，可选
                    ''',re.VERBOSE)
    print(re.search(r,str2).group())

if __name__ == "__main__":
    re_method()


