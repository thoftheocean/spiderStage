# !/usr/bin/env python
# coding:utf-8
# author hx
import urllib2
import re
import os
# 抓取糗事百科上面的文字
if __name__ == '__main__':
    # 抓取所有的页面的内容
    print '开始抓取内容咯'
    for page in range(1, 35):
        # 抓取过程
        # 1访问其中一个网页地址，获取源代码
        url = 'http://www.qiushibaike.com/8hr/page/'+str(page)+'/?s=4968934'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
        try:
            request = urllib2.Request(url=url, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
        except urllib2.HTTPError as e:
            print e
            exit()
        except urllib2.URLError as e:
            print e
            exit()
        # 2根据抓取的网页源代码，提取数据
        # regex = re.compile('<div class="content">(.*?)<!--(.*?)-->(.*?)</div>', re.s)
        # .*?匹配任意字符（非贪婪模式。匹配成功后不继续向更长的字符进行匹配），加了re.S之后就会.也可以输出换行
        pattern = re.compile('<div class="content">(.*?)<span>(.*?)</span>(.*?)</div>', re.S)

        items = re.findall(pattern, content)
        num = 1
        for item in items:
            item_new = item[1].replace('<br/>', '')
            # 将<br/>的换行，换成\n的换行
            print '第'+str(num)+'条'+item_new
            # 保存抓取的数据
            path = 'qishi'
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/' + 'jokes' + str(page) + '_' + str(num) + '.txt'
            f = open(file_path, 'w')
            f.write(item_new)
            f.close()
            num += 1
    print '数据抓取完了'