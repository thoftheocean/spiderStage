import urllib
import requests
import urllib2

url ='https://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E5%88%9B%E6%84%8F%E6%91%84%E5%BD%B1&oriquery=%E5%BE%AE%E8%B7%9D%E6%91%84%E5%BD%B1&ofr=%E5%BE%AE%E8%B7%9D%E6%91%84%E5%BD%B1'
# url =urllib.urlencode(url)
print (url)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
r = requests.get(url=url,headers=headers)
with open('1.txt','a+') as f:
    f.write(r.content)
print (r.content)
# parser = MovieParser()
# parser.feed(r.content)
# r.close()
# return arser.movies

