# !/usr/bin/env python
# coding:utf-8
# author hx
import urllib2
import re
import os
# 抓取糗事百科上面的文字
class Spider(object):
    # 构造方法
    def __init__(self):
        self.url = 'http://www.qiushibaike.com/8hr/page/%s/?s=4968934'
        self.user_agent ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
    # 获取网页源代码
    def get_page(self, page_index):
        headers = {'User-Agent': self.user_agent}
        try:
            request = urllib2.Request(url=self.url % str(page_index), headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except urllib2.HTTPError as e:
            print e
            exit()
        except urllib2.URLError as e:
            print e
            exit()

    # 分析源代码
    def analysis(self, content):
        pattern = re.compile('<div class="content">(.*?)<span>(.*?)</span>(.*?)</div>', re.S)
        items = re.findall(pattern, content)
        return items

    # 保存数据
    def save(self, items, path, page_index):
        num=1
        for item in items:
            item_new = item[1].replace('<br/>', '')
            # 将<br/>的换行，换成\n的换行
            print '第' + str(num) + '条' + item_new
            # 保存抓取的数据
            # path = 'qishi'
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/' + 'jokes' + str(page_index) + '_' + str(num) + '.txt'
            f = open(file_path, 'w')
            f.write(item_new)
            f.close()
            num += 1

    # 运行
    def run(self):
        print '开始抓内容咯'
        for i in range(1, 35):
            content = self.get_page(i)
            items = self.analysis(content)
            self.save(items, 'qiubai', i)
        print '抓取内容完咯'
if __name__ == '__main__':
    spider = Spider()
    spider.run()

