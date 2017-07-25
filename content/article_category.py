#coding=utf8
import requests
from bs4 import BeautifulSoup
from  database import dbUtil
import lxml
from model import DBSession as db
import time,random
import random
import socket
import struct

session = db.DBSession()


def get_category():
    category_url = "http://www.ruanyifeng.com/blog/archives.html"
    r = requests.get(category_url)
    # print r.content
    soup = BeautifulSoup(r.content)
    # tag_list = soup.select('.module-list-item')
    for tag in soup.select('#beta-inner li'):
        # print tag.get_text()
        category = db.BlogCategory(href=tag.a.get('href'),tag_name=tag.a.text)
        session.add(category)
    session.commit()
    session.close()


def get_article():
    tag_list = session.query(db.BlogCategory).all()
    for item in tag_list[1:]:
        soup = get_content(item.href)
        for article_url in soup.select('#alpha-inner .module-list-item'):
            link = article_url.a.get('href')
            title = article_url.a.get_text()
            print link,title
            article_soup = get_content(link)
            content = article_soup.select('#main-content')
            article = db.Article(link = link, title = title, content= content[0].extract(),tag_id = item.id)
            session.add(article)
            session.commit()
    session.close()


def get_content(url):
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
               'hosts': random_ip()}
    time.sleep(random.sample(xrange(1,3),1)[0])
    while True:
        try:
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content)
            r.close()
            break
        except :
            time.sleep(5)
    return soup


def random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

if __name__ == '__main__':
    get_article()