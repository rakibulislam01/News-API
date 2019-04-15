import newspaper


# popular newspapers url
def popular_paper():
    popular_url = newspaper.popular_urls()
    return popular_url


# hot news
def hot_news():
    hot_topic = newspaper.hot()
    return hot_topic
