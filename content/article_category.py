import requests
from bs4 import BeautifulSoup
from  database import dbUtil
import lxml



def get_category():
    category_url = "http://www.ruanyifeng.com/blog/archives.html"
    r = requests.get(category_url)
    # print r.content
    soup = BeautifulSoup(r.content)
    print soup.prettify()
    # tag_list = soup.select('.module-list-item')
    for tag in soup.select('#beta-inner li'):
        # print tag.get_text()
        print tag.a
        print tag.a.get('href')




if __name__ == '__main__':
    get_category()
