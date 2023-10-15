import requests


class NewsFeed:
    """Representing multiple news titles and links as a single string
    """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "a9c14d7269894d69bc39c744037fa4ca"

    def __init__(self, interest, from_date, to_date, language="en"):
        self.language = language
        self.to_date = to_date
        self.from_date = from_date
        self.interest = interest

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ""
        for article in articles:
            email_body += article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}qInTitle={self.interest}&from={self.from_date}&to={self.to_date}&language={self.language}&apiKey={self.api_key}"
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(interest="nasa", from_date="2023-10-14", to_date="2023-10-15", language="en")
    print(news_feed.get())
