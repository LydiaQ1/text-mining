from newspaper import Article
import nltk   # install the Natural Language Toolkit
nltk.download('punkt')   # Punkt Sentence Tokenizer divides a text into a list of sentences
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys
from unicodedata import category

"""
Functions below are to have a general overview at the important features of the news article, on aspects include: title,
author, publish date, url, keywords, and summary.
"""
url = 'https://abcnews.go.com/Politics/biden-takes-office-turn-page-rolling-back-trump/story?id=75343545'
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
#print(article.text)

def most_common(s):
    """
    This function will return dictionary with words in the text and how many time each of them have appeared, the words will be 
    sorted from a descending frequency.
    """
    d = dict()
    text_d = s.split
    for word in text_d():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    text_new = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return text_new


def stop_words(filename):
    """
    This function will return dictionary with words in an appointed file (which will be addressed in the code below).
    """
    f = open(filename, encoding = 'UTF8')
    stop_word_d = {}
    for line in f:
        word = line.strip()
        strop_word_d[word] = 0
    return stop_word_d

def main():
    """
    The functions below will return final output, which is the words in text with the values of how 
    many times they've appeared in a descending order, without stopwords in the stopwords.txt file.
    """
    text = article.text
    filename = open("/Users/z/Desktop/2022 Fall/OIM/text-mining/Assignments/stopwords.txt","r")
    d = stop_words(filename)
    freq = most_common(text)

if __name__ == "__main__":
    main()

"""
Functions below are for Sentiment Intensity Analysis of the text, to see the percentage of positive/neutral/negative/compound
words used in the text.
"""
sentence = article.text
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)


