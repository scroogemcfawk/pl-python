from Article import Article
from ForbesScraper import ForbesScraper
from HabrScraper import HabrScraper
from VtomskeScraper import VtomskeScraper


class Aggregator:
    def __init__(self):
        self.habr_scraper = HabrScraper("https://habr.com/ru/news/")
        self.forbes_scraper = ForbesScraper("https://www.forbes.ru/")
        self.vtomske_scraper = VtomskeScraper("https://news.vtomske.ru/c/tomsk")

    def get_articles(self) -> list[Article]:
        articles = []

        for a in self.habr_scraper.get_articles():
            articles.append(a)
        for a in self.forbes_scraper.get_articles():
            articles.append(a)
        for a in self.vtomske_scraper.get_articles():
            articles.append(a)

        return articles


if __name__ == "__main__":
    a = Aggregator()
    print(*a.get_articles(), sep="\n")
