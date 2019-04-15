from urllib.request import urlopen

from bs4 import BeautifulSoup as soup


def top_news_korean():
    news_url = "http://feeds.bbci.co.uk/korean/rss.xml"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()

    soup_page = soup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    news_all = []
    news_dic = {}
    news_link = []
    for news in news_list:
        text = news.title.text
        link = news.link.text
        news_all.append(text)
        news_link.append(link)

        news_dic = dict(zip(news_all, news_link))

    return news_dic

# top_news_title()
