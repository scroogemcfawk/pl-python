import requests

from Article import Article
from Scraper import Scraper, ArticleFetcher


class VtomskeArticleFetcher(ArticleFetcher):

    def get_articles(self) -> list[Article]:
        articles = []
        for article in self.bs.find(name="div", class_="article-list").find_all("a"):
            author = "news.vtomske.ru"
            title = article.find("div", class_="title").find(string=True, recursive=False)
            annotation = "https://" + author + article["href"]
            articles.append(Article(title, annotation, [author], author))
        return articles


class VtomskeScraper(Scraper):

    def get_articles(self) -> list[Article]:
        html = requests.get(self.base_url).text
        fetcher = VtomskeArticleFetcher(html)
        return fetcher.get_articles()


if __name__ == "__main__":
    s = VtomskeScraper("https://news.vtomske.ru/c/tomsk")
    print(*s.get_articles(), sep="\n")
