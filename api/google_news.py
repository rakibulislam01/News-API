from urllib.request import urlopen
import datetime
from bs4 import BeautifulSoup as soup
from time import gmtime, strftime


def top_news_title():
    # news_url = "https://news.google.com/news/rss/"
    news_url = "https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US:en"
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
        daten = date.split( )
        string = ' '.join(daten[0:4])
        stime = strftime("%a, %d %b %Y", gmtime())
        if string == stime:
            news_date.append(date)
            news_all.append(text)
            news_dic = dict(zip(news_all, news_date))

    return news_dic


def top_education_news():
    news_url = "https://news.google.com/rss/topics/CAAqBwgKMJG69QowpazcAg?hl=en-US&gl=US&ceid=US:en"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    news_all = []
    for news in news_list[:10]:
        text = news.title.text
        link = news.link.text
        date = news.pubDate.text

        news_all.append(text)

    return news_all