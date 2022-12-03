from types import new_class

from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer

MEDIAS = {
    "abc": [
        "https://abcnews.go.com/Politics/biden-takes-office-turn-page-rolling-back-trump/story?id=75343545",
    ],
    "fox": [
        "https://www.foxnews.com/politics/bidens-inauguration-everything-you-need-to-know",
    ],
        "new yorker": [
        "https://www.newyorker.com/news/letter-from-bidens-washington/joe-bidens-love-letter-to-the-truth",
    ],
}


def get_artile(url):
    """Given an url, return the text of article"""
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    title = article.title
    author = article.authors
    publish_date = article.publish_date
    summary = article.summary
    keywords = article.keywords
    text = article.text
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Publish Date: {publish_date}")
    print(f"URL: {url}")
    print(f"Keywords: {keywords}")
    print(f"Summary: {summary}")
    return text

def get_sentiment_score(text):
    """
    Functions below are for Sentiment Intensity Analysis of the text, to see the percentage of positive/neutral/negative/compound
    words used in the text.
    """
    sentence = text
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return score


def main():
    res = {} 

    for media, urls in MEDIAS.items():
        res[media] = []
        for url in urls:
            text = get_artile(url)
            sentiment_score = get_sentiment_score(text)
            res[media].append(sentiment_score)

    print(res)


if __name__ == "__main__":
    main()

