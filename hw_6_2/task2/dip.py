class NewsPaper:
    """Клас газети, яка вміє публікувати новини"""

    def publish(self, news: str) -> None:
        print(f"{news} published today")


class Reporter:
    """Репортер, який залежить від об'єкта з методом publish"""

    def __init__(self, publisher) -> None:
        self.publisher = publisher

    def publish(self, news: str) -> None:
        self.publisher.publish(news)


# Використання
news_paper = NewsPaper()
reporter = Reporter(news_paper)
reporter.publish("News Paper")