# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境
import urllib
import requests
from HTMLParser import HTMLParser
import re


def _attr(attrs,attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None

class PoemParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tangshi_list = []
        self.in_div = False
        self.in_a = False
        self.pattern = re.compile(r'''
                                    (.+)  #匹配标题 group(1)
                                    \(    #匹配作者左边的括号
                                    (.+)  #匹配作者 group(2)
                                    \)    #匹配作者右边的括号
                                    ''',re.VERBOSE)
        self.current_poem = {}
    def handle_starttag(self, tag, attrs):
        if tag == 'div' and _attr(attrs,'class') == 'guwencont2':
            self.in_div = True
        if self.in_div and tag =='a':
            self.in_a = True
            self.current_poem['url'] = _attr(attrs,'href')
    def handle_endtag(self, tag):
        if tag == 'div':
            self.in_div = False

        if tag == 'a':
            self.in_a = False

    def handle_data(self, data):
        if  self.in_a:
            print (data)
            m = self.pattern.match(data)
            if m:
                self.current_poem['title'] = m.group(1)
                self.current_poem['author'] = m.group(2)
                self.tangshi_list.append(self.current_poem)
                self.current_poem = {}



def retrive_tangshi_300():
    url = 'http://www.gushiwen.org/gushi/tangshi.aspx'
    r = requests.get(url)
    p = PoemParser()
    p.feed(r.content)
    return p.tangshi_list


if __name__ == "__main__":
    l = retrive_tangshi_300()
    print ('total %s poems.' % len(l))
    for  i in range(10):
        print ('标题: %(title)s\t 作者：%(author)s\tURL:%(url)s' % (l[i]))