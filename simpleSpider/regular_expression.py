# !/usr/bin/env python
# coding:utf-8
# author hx

# 判断一个字符串是否全都是小写字母

# import re
# if __name__=='__main__':
#     # 1.判断一个字符串是否全都是小写字母
#     str1 = 'deskesldje'
#     an = re.match('[a-z]+$', str1)
#     if an:
#         print '全是小写'
#     else:
#         print '不全是小写'
# print an
# print an.group()  # 直接输出deskesldje

2
# import re
# if __name__=='__main__':
#     # # 1.判断一个字符串是否全都是小写字母
#     str1 = 'deskesldje'
#     an = re.search('^[a-z]+$', str1) # search中加上边界符^
#     if an:
#         print '全是小写'
#     else:
#         print '不全是小写'
# print an

# 3

# import re
# if __name__ == '__main__':
#     # # 1.判断一个字符串是否全都是小写字母
#     str1 = 'dfdgd'
#     str2 = re.compile('^[a-z]+$') # 对正则表达式进行编译
#     an = str2.search(str1) # search中加上边界符^,从头开始查找
#     if an:
#         print '全是小写'
#     else:
#         print '不全是小写'
# print an.group()

# group 提取分组字符串

# import re
# if __name__ == '__main__':
#     # # 1.判断一个字符串是否全都是小写字母
#     str1 = '4454kesl123245slfsdlfdlg'
#     # str2 = re.compile('([0-9]+)([a-z]+)([0-9]+)([a-z]+)')
#     # obj = str2.search(str1)
#     obj = re.search('([0-9]+)([a-z]+)([0-9]+)([a-z]+)', str1) #serch是从任意位置查找，加上^就是从开始查找
#     print obj.group()

#4 从字符串中提取邮箱和手机号
# import re
# if __name__ == '__main__':
#     # # 1.判断一个字符串是否全都是小写字母
#     str1 = '这是一个字符串15280236583jdfjd1848500475@qq.com13245454'
#     regex_phone = re.compile('((?:(?:13[0-9])|(?:15[^4,\D])|(?:18[0,2,5-9]))\d{8})')  # 对不想分组的地方加？：
#     regex_email = re.compile('((?:[0-9]+)@(?:[a-z]+)(?:\.[a-z]+))')
#     print regex_phone.findall(str1)
#     print regex_email.findall(str1)

#
# import re
# if __name__ == '__main__':
#     # # 1.判断一个字符串是否全都是小写字母
#     str1 = '这是一个字符串15280236583jdfjd1848500475@qq.com13245454'
#     regex = re.compile('(?:\d{11}|(?:(?:[0-9]+)@(?:[a-z]+)(?:\.[a-z]+)))')  # 对不想分组的地方加？：
#     print regex.findall(str1)



# 5字符串分离

# import re
# if __name__ == '__main__':
#     str1 = '4454kesl123245slfsdlfdlg'
#     # str2 = re.compile('([0-9]+)([a-z]+)([0-9]+)([a-z]+)')
#     # obj = str2.search(str1)
#     obj = re.split('([0-9]+)', str1)
#     print obj

# 字符串替换

# import re
# if __name__ == '__main__':
#     str1 = '4454kesl123245slfsdlfdlg'
#     obj1 = re.sub('([0-9]+)', '234', str1)
#     obj2 = re.subn('([a-z]+)', 'abc', str1)
#     print obj1
#     print obj2
#
