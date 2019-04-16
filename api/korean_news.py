from urllib.request import urlopen
import datetime
from bs4 import BeautifulSoup as soup
from time import gmtime, strftime


# CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako
# https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFp4WkRNU0FtVnVLQUFQAQ?hl=ko&gl=KR&ceid=KR%3Ako


# korean news from bbc
def bbc_korean_news():
    news_url = "http://feeds.bbci.co.uk/korean/rss.xml"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    news_all = []
    news_date = []
    news_dic = {}
    news_link = []
    for news in news_list:
        text = news.title.text
        link = news.link.text
        date = news.pubDate.text
        daten = date.split()
        string = ' '.join(daten[0:4])
        stime = strftime("%a, %d %b %Y", gmtime())
        if string == stime:
            news_date.append(date)
            news_all.append(text)
            news_link.append(link)
            news_dic = []
            for i in range(len(news_all)):
                test = {'headline': news_all[i], 'link': news_link[i]}
                news_dic.append(test)

    return news_dic


# World latest news
def world_korean_news():
    news_url = "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    news_all = []
    news_date = []
    news_dic = {}
    news_link = []
    for news in news_list:
        text = news.title.text
        link = news.link.text
        date = news.pubDate.text
        daten = date.split()
        string = ' '.join(daten[0:4])
        stime = strftime("%a, %d %b %Y", gmtime())
        if string == stime:
            news_date.append(date)
            news_all.append(text)
            news_link.append(link)
            news_dic = []
            for i in range(len(news_all)):
                test = {'headline': news_all[i], 'link': news_link[i]}
                news_dic.append(test)

    return news_dic


# Korean latest news from google
def google_korean_news():
    # news source "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFp4WkRNU0FtVnVLQUFQAQ?hl=ko&gl=KR&ceid=KR%3Ako"
    news_url = "https://news.google.com/rss/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFp4WkRNU0FtVnVLQUFQAQ?hl=ko&gl=KR&ceid=KR%3Ako"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    news_all = []
    news_date = []
    news_dic = {}
    news_link = []
    for news in news_list:
        text = news.title.text
        link = news.link.text
        date = news.pubDate.text
        daten = date.split()
        string = ' '.join(daten[0:4])
        stime = strftime("%a, %d %b %Y", gmtime())
        if string == stime:
            news_date.append(date)
            news_all.append(text)
            news_link.append(link)
            news_dic = []
            for i in range(len(news_all)):
                test = {'headline': news_all[i], 'link': news_link[i]}
                news_dic.append(test)

    return news_dic


def korean_sports_news():
    # news_url = "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"
    news_url = "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR&ceid=KR%3Ako"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    news_all = []
    news_date = []
    news_dic = {}
    news_link = []
    for news in news_list:
        text = news.title.text
        link = news.link.text
        date = news.pubDate.text
        daten = date.split()
        string = ' '.join(daten[0:4])
        stime = strftime("%a, %d %b %Y", gmtime())
        if string == stime:
            news_date.append(date)
            news_all.append(text)
            news_link.append(link)
            news_dic = []
            for i in range(len(news_all)):
                test = {'headline': news_all[i], 'link': news_link[i]}
                news_dic.append(test)

    return news_dic
