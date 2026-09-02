from news_article import NewsArticle


class NewsPortal:
    def __init__(self):
        self.__published_articles = []

    def publish_article(self, article):
        is_valid = self.__is_valid_article(article)

        if is_valid:
            current_title = article.get_title()
            current_author = article.get_author()
            print(f'Статья "{current_title}", опубликована автором {current_author}')
            self.__published_articles.append(article)
        else:
            print('Ошибка. Некорректные данные')
            return

    def __is_valid_article(self, article):
        if not isinstance(article, NewsArticle):
            return False
        else:
            return True
