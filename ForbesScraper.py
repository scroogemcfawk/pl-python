from Article import Article
from Scraper import Scraper, ArticleFetcher
import requests


class ForbesArticleFetcher(ArticleFetcher):

    def get_articles(self) -> list[Article]:
        articles = []
        for article in self.bs.find_all(name="div", class_="Sa7ru"):
            try:
                annotation = ""
                temp_title = article.find("div", class_="MhD5o")
                if temp_title is None:
                    temp_title = article.find("div", class_="XjpMy")
                    if temp_title is None:
                        temp_title = article.find("p", class_="fMXqV")
                    else:
                        annotation = article.find("p", class_="fMXqV")

                if annotation is None or annotation == "":
                    try:
                        annotation = "https://forbes.ru" + article.find("a", class_="gwrtL")["href"].strip()
                    except:
                        annotation = "-"
                else:
                    annotation = annotation.text
                title = temp_title.text
                title = title.strip()
                annotation = annotation.strip()

                try:
                    author = article.find("p", class_="_43QGD").text
                except:
                    author = "Forbes"

                articles.append(Article(title, annotation=annotation, authors=[author], source="Forbes.ru"))
            except:
                continue

        return articles


class ForbesScraper(Scraper):

    def get_articles(self) -> list[Article]:
        html = requests.get(self.base_url).text
        fetcher = ForbesArticleFetcher(html)
        return fetcher.get_articles()


if __name__ == "__main__":
    scraper = ForbesScraper("https://www.forbes.ru/")
    print(*scraper.get_articles(), sep="\n")
