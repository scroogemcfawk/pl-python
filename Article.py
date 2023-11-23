class Article:

    def __init__(
            self,
            title: str = "No title",
            annotation: str = "",
            authors: list = None,
            source: str = "Unknown Source"
    ):
        if authors is None:
            authors = []
        self.title = title
        self.annotation = annotation
        self.authors = authors
        self.source = source

    def __str__(self) -> str:
        return f"{self.source}\n{self.title}\nby {', '.join(self.authors)}\n{self.annotation}\n"


if __name__ == "__main__":
    a = Article("Clickbait", "This is a clickbait article.", ["Troll"])
    print(a)
    assert a.title == "Clickbait"
    assert a.annotation == "This is a clickbait article."
    assert a.authors == ["Troll"]
