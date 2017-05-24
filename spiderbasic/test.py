# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境
import urllib2
from HTMLParser import HTMLParser
import urllib
import requests

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        # self.in_movies = False

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

    #     if tag == 'li' and _attr(attrs, 'data-title') and _attr(attrs,'data-category')=='nowplaying':
    #         movie ={}
    #         movie['title'] = _attr(attrs, 'data-title')
    #         movie['score'] = _attr(attrs, 'data-score')
    #         movie['director'] = _attr(attrs, 'data-director')
    #         movie['actors'] = _attr(attrs, 'data-actors')
    #         self.movies.append(movie)
    #         print('%(title)s\t|%(score)s\t|%(director)s\t|%(actors)s' % movie)
    #         self.in_movies = True
    #     if tag == 'img' and self.in_movies:
    #         self.in_movies = False
    #         src = _attr(attrs,'src')
    #         movie = self.movies[len(self.movies)-1]
    #         movie['poster-url']=src
    #         _download_poster_image(movie)

        if tag == 'img' and _attr(attrs, 'src') and _attr(attrs,'onload')=="window.speed.loadmark();":
            movie = {}
            movie['url1'] = _attr(attrs, 'src')
            self.movies.append(movie)
            # src = _attr(attrs, 'src')
            # movie = self.movies[len(self.movies)-1]
            # movie['url']=src
            _download_poster_image(movie)
# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境

def _download_poster_image(movie):
    src = movie['url1']
    r = requests.get(src)
    fname =src.split('/')[-1]
    with open('img_movies/'+fname,'wb') as f:
        f.write(r.content)
        # movie['url'] = fname


def nowplaying_movies():
    url = 'https://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E5%88%9B%E6%84%8F%E6%91%84%E5%BD%B1&oriquery=%E5%BE%AE%E8%B7%9D%E6%91%84%E5%BD%B1&ofr=%E5%BE%AE%E8%B7%9D%E6%91%84%E5%BD%B1'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
    r = requests.get(url=url,headers=headers)
    print (r.content)
    parser = MovieParser()
    parser.feed(r.content)
    r.close()
    return parser.movies

if __name__ == '__main__':
    movies = nowplaying_movies()

    # import json
    # print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',', ': ')))
















