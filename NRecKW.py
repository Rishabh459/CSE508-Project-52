import tweepy
import requests
from rake_nltk import Rake
from collections import defaultdict
import json
import os
from nltk.corpus import stopwords
import pandas as pd

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# News API key
news_api_key = "your_news_api_key"

# Initialize Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get user's p most recent tweets
def get_tweets(username, p):
    tweets = api.user_timeline(screen_name=username, count=p)
    return [tweet.text for tweet in tweets]

# Extract keywords from tweets
def extract_keywords(tweets):
    r = Rake(stopwords=stopwords.words("english"), punctuations=".,;:!?(){}[]<>/\\")
    keywords = []
    for tweet in tweets:
        r.extract_keywords_from_text(tweet)
        keywords.extend(r.get_ranked_phrases())
    return keywords

# Get news articles using keywords
def get_news_articles(keywords):
    # url = f"https://newsapi.org/v2/everything?q={'+'.join(keywords)}&apiKey={news_api_key}"
    # response = requests.get(url)
    # return response.json()["articles"]
    # load from folder with json files
    news_articles = []
    for filename in os.listdir("NEWS_ARTICLES"):
        if filename.endswith(".json"):
            with open(os.path.join("NEWS_ARTICLES", filename), "r") as f:
                news_articles_i = json.load(f)
                news_articles.extend(news_articles_i['articles'])
    return news_articles

# # Rank articles based on keyword matches
# def rank_articles(articles, keywords):
#     ranked_articles = defaultdict(int)
#     for article in articles:
#         for keyword in keywords:
#             ranked_articles[article["url"]] += article["title"].lower().count(keyword.lower())
#             if article["description"] is not None:
#                 ranked_articles[article["url"]] += 0.8*article["description"].lower().count(keyword.lower())
#             if article["content"] is not None:
#                 ranked_articles[article["url"]] += 0.5*article["content"].lower().count(keyword.lower())
#             # if keyword.lower() in article["description"].lower():
#                 # ranked_articles[article["url"]] += 0.8
#     return sorted(ranked_articles.items(), key=lambda x: x[1], reverse=True)


from textblob import TextBlob

# ...

def rank_articles(articles, keywords):
    
    ranked_articles = defaultdict(int)

    for article in articles:
        title_sentiment = TextBlob(article["title"]).sentiment.polarity
        if article["description"] is not None:
            desc_sentiment = TextBlob(article["description"]).sentiment.polarity
        else:
            desc_sentiment = 0
        if article["content"] is not None:
            content_sentiment = TextBlob(article["content"]).sentiment.polarity
        else:
            content_sentiment = 0
        sentiment_score = (title_sentiment + 0.8*desc_sentiment + 0.5*content_sentiment) / 2.3  # normalize
        sentiment_score = (title_sentiment + 0.8*desc_sentiment) / 1.8

        for keyword in keywords:
            ranked_articles[article["url"]] += sentiment_score * article["title"].lower().count(keyword.lower())
            if article["description"] is not None:
                ranked_articles[article["url"]] += 0.8*sentiment_score*article["description"].lower().count(keyword.lower())
            # if article["content"] is not None:
            #     ranked_articles[article["url"]] += 0.5*sentiment_score*article["content"].lower().count(keyword.lower())
    return sorted(ranked_articles.items(), key=lambda x: x[1], reverse=True)


def get_tweets(username):
    os.chdir('tweets')
    df = pd.read_csv(username  + '.csv')
    os.chdir('..')
    return df['text'].tolist()

# Recommend top k articles
def recommend_articles(username, p, k):
    tweets = get_tweets('gretaData')
    # get tweets polarity cumulative score
    tweets_polarity = 0
    for tweet in tweets:
        tweets_polarity += TextBlob(tweet).sentiment.polarity
    tweets_polarity /= len(tweets)

    

    keywords = extract_keywords(tweets)
    articles = get_news_articles(keywords)
    # print(articlezz)
    # articles = []
    # for art in articlezz:
    #     article = ""
    #     if art['title'] is not None:
    #         article += art['title']
    #     if art['description'] is not None:
    #         article += art['description']
    #     if art['content'] is not None:
    #         article += art['content']
    #     articles.append(article)
        
    ranked_articles = rank_articles(articles, keywords)
    return (ranked_articles[:k]+ranked_articles[-k:], tweets_polarity)

if __name__ == "__main__":
    username = "example_user"
    p = 10
    k = 11
    recommended_articles, tweets_polarity = recommend_articles(username, p, k)
    print("Top", k, "recommended articles of similar opinion:")
    same_polarity = [article for article in recommended_articles if article[1]*tweets_polarity >= 0]
    opposite_polarity = [article for article in recommended_articles if article[1]*tweets_polarity < 0]
    opposite_polarity.reverse()
    i = 0
    for article in same_polarity:
        i+=1
        print(i, end = ". ")
        print(article)
    print()
    print("Top", k, "recommended articles of contrary opinion:")
    i = 0
    for article in opposite_polarity:
        i+=1
        print(i, end = ". ")
        print(article)