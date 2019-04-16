from urllib.request import urlopen
import datetime
from bs4 import BeautifulSoup as soup
from time import gmtime, strftime


def top_news_korean():
    news_url = "http://feeds.bbci.co.uk/korean/rss.xml"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    news_all = []
    news_date = []
    news_dic = {}
    for news in news_list:
        text = news.title.text
        # link = news.link.text
        date = news.pubDate.text
        print(date)
        daten = date.split( )
        string = ' '.join(daten[0:4])
        stime = strftime("%a, %d %b %Y", gmtime())
        if string == stime:
            news_date.append(date)
            news_all.append(text)
            news_dic = dict(zip(news_all, news_date))

    return news_dic


def top_news_korean_times():
    news_url = "http://www.koreatimes.co.kr/www/rss/rss.xml"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    news_all = []
    news_date = []
    news_dic = {}
    for news in news_list:
        text = news.title.text
        # link = news.link.text
        date = news.pubdate.text
        daten = date.split( )
        string = ' '.join(daten[0:3])
        print("newsdate", string)
        stime = strftime("%a, %b %Y", gmtime())
        print("mydate",stime)
        if string == stime:
            news_date.append(date)
            news_all.append(text)
            news_dic = dict(zip(news_all, news_date))

    return news_dic