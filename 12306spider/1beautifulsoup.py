#coding:utf-8
from bs4 import BeautifulSoup


with open('1.html','r') as f:
    s = f.read()
    soup = BeautifulSoup(s)
    # print soup.name
    # print soup.head.name
    print soup.p.string




