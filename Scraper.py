from abc import abstractmethod

import bs4
import requests

from Article import Article


class Scraper:
    def __init__(self, base_url):
        assert requests.get(base_url).status_code == 200
        self.base_url = base_url

    @abstractmethod
    def get_articles(self) -> list[Article]:
        raise Exception("Not Implemented")


class ArticleFetcher:
    def __init__(self, html):
        self.bs = bs4.BeautifulSoup(html, features="html.parser")

    @abstractmethod
    def get_articles(self) -> list[Article]:
        raise Exception("Not Implemented")
