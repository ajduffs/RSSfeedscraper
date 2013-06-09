import feedparser
from sys import argv

script, filename = argv

urllist = ["http://www.abc.net.au/news/feed/45910/rss.xml"]
#["",""]
#https://news.google.com.au/news/feeds?q=mining&num=50&cr=countryAU&safe=off&hl=en&gl=au&biw=1920&bih=965&um=1&ie=UTF-8&output=rss
#http://feeds.smh.com.au/rssheadlines/national.xml

f = open(filename, 'w')

for url in urllist:
    feed=feedparser.parse(url)
    for e in feed.entries:
        f.write(e.link.encode('ascii', 'ignore'))
        f.write("\n")

f.close()



"""
Scrapes any number of RSS feeds and dumps the links in a seperate file. If run multiple times the script may produce
a list with duplicate links. Cleaner.py is designed to deal with the duplication
"""

