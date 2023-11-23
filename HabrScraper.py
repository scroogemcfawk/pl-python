from Article import Article
from Scraper import Scraper
import requests
import bs4


class HabrArticleFetcher:

    def __init__(self, html):
        self.bs = bs4.BeautifulSoup(html, features="html.parser")

    def get_articles(self) -> list[Article]:
        articles = []
        for article in self.bs.find_all(name="article"):
            author = article.find("a", class_="tm-user-info__username").text.strip()
            temp_title = article.find("h2", class_="tm-title")
            title = temp_title.text.strip()
            # Headless browser is needed to load dynamic content, but it's too boring
            annotation = "https://habr.com" + temp_title.find("a")["href"]
            articles.append(Article(title, annotation=annotation, authors=[author], source="Habr.com"))
        return articles


class HabrScraper(Scraper):

    def __init__(self, base_url: str):
        assert requests.get(base_url).status_code == 200
        self.base_url = base_url

    def get_articles(self) -> list[Article]:
        html = requests.get(self.base_url).text
        fetcher = HabrArticleFetcher(html)
        return fetcher.get_articles()


if __name__ == "__main__":
    scraper = HabrScraper("https://habr.com/ru/news/")
    print(*scraper.get_articles())

