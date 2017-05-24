# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境
import urllib2
from HTMLParser import HTMLParser

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        if tag == 'li' and _attr(attrs, 'data-title') and _attr(attrs,'data-category')=='nowplaying':
            movie ={}
            movie['title'] = _attr(attrs, 'data-title')
            movie['score'] = _attr(attrs, 'data-score')
            movie['director'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            self.movies.append(movie)
            print('%(title)s|%(score)s|%(director)s|%(actors)s' % movie)

def nowplaying_movies():
    url = 'https://movie.douban.com/cinema/nowplaying/chengdu/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    s = urllib2.urlopen(req)
    parser = MovieParser()
    parser.feed(s.read())
    s.close()
    return parser.movies

if __name__ == '__main__':
    movies = nowplaying_movies()

    # import json
    # print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',', ': ')))