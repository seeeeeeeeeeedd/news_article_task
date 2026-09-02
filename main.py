from news_article import NewsArticle
from news_portal import NewsPortal

news_portal = NewsPortal()

news_article1 = NewsArticle('Первый шаг', 'Анна Сергеева')
news_portal.publish_article(news_article1)

news_article2 = NewsArticle('', 'Ольга Смирнова')
news_portal.publish_article(news_article2)

news_article3 = NewsArticle('Дорога домой', 23)
news_portal.publish_article(news_article3)
