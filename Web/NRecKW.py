import tweepy
from rake_nltk import Rake
from collections import defaultdict
import json
import os
import nltk
from nltk.corpus import stopwords
from yake import KeywordExtractor
import numpy as np
from keybert import KeyBERT
from textblob import TextBlob
import pandas as pd
nltk.download('stopwords')
import textacy

# Extract keywords from tweets
def extract_keywords(tweets):
    r = Rake(stopwords=stopwords.words("english"), punctuations=".,;:!?(){}[]<>/\\")
    keywords = []
    for tweet in tweets:
        r.extract_keywords_from_text(tweet)
        keywords.extend(r.get_ranked_phrases())
    return keywords

# use keybert to extract keywords
def extract_keywords_bert(tweets):
    model = KeyBERT('distilbert-base-nli-mean-tokens')
    keywords = []
    for tweet in tweets:
        keyword_list = model.extract_keywords(tweet, keyphrase_ngram_range=(1, 1), stop_words='english', top_n=min(12, int(len(tweet.split())/2)))
        keywords.extend([keyphrase[0] for keyphrase in keyword_list])
    # remove stopwords
    keywords = [keyword for keyword in keywords if keyword not in stopwords.words("english")]
    keywords = list(set(keywords))
    print(keywords)

    return keywords

# use YAKE to extract keywords
def extract_keywords_yake(tweets):
    keywords = []
    for tweet in tweets:
        kw_extractor = KeywordExtractor(lan="en", n=1, top=min(12, int(len(tweet.split())/2)))
        keywords_yake = kw_extractor.extract_keywords(tweet)
        keywords.extend([keyphrase[0] for keyphrase in keywords_yake])
    return keywords


# textacy to extract keywords
def extract_keywords_textacy(tweets):
    keywords = []
    for tweet in tweets:
        doc = textacy.make_spacy_doc(tweet, lang="en_core_web_sm")
        noun_chunks = textacy.extract.noun_chunks(doc, min_freq=1)
        keywords.extend([chunk.text for chunk in noun_chunks if chunk.text not in stopwords.words("english") and len(chunk.text) > 3])
    keywords = list(set(keywords))
    return keywords


# Get news articles using keywords
def get_news_articles(keywords):
    news_articles = []
    for filename in os.listdir("News Articles"):
        if filename.endswith(".json"):
            with open(os.path.join("News Articles", filename), "r") as f:
                news_articles_i = json.load(f)
                news_articles.extend(news_articles_i['articles'])
    return news_articles

# Rank news articles using keywords
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
            ranked_articles[(article["url"], article["title"])] += sentiment_score * article["title"].lower().count(keyword.lower())
            if article["description"] is not None:
                ranked_articles[(article["url"], article["title"])] += 0.8*sentiment_score*article["description"].lower().count(keyword.lower())
            # if article["content"] is not None:
            #     ranked_articles[article["url"]] += 0.5*sentiment_score*article["content"].lower().count(keyword.lower())
    return sorted(ranked_articles.items(), key=lambda x: x[1], reverse=True)


def get_tweetss(username):
    name = username + '.csv'
    df = pd.read_csv(name)
    tweets = df['Tweet'].tolist()
    return tweets

# Recommend top k articles
def recommend_articles(username, k, kwe_metric):
    diction = {'Greta Thunberg': 'gretaData', 'Virat Kohli': 'kohliData', 'Sundar Pichai': 'pichaiData', 'Samay Raina': 'samayData', 'Narendra Modi' : 'modiData'}
    username = diction[username]
    tweets = get_tweetss(username)
    
    # get tweets polarity cumulative score
    tweets_polarity = 0
    for tweet in tweets:
        tweets_polarity += TextBlob(tweet).sentiment.polarity
    tweets_polarity /= len(tweets)

    # extract keywords
    if kwe_metric == 1:
        keywords = extract_keywords_yake(tweets)
        articles = get_news_articles(keywords)
    elif kwe_metric == 2:
        keywords = extract_keywords(tweets)
        articles = get_news_articles(keywords)
    elif kwe_metric == 3:
        keywords = extract_keywords_bert(tweets)
        articles = get_news_articles(keywords)
    elif kwe_metric == 4:
        keywords = extract_keywords_textacy(tweets)
        articles = get_news_articles(keywords)

    ranked_articles = rank_articles(articles, keywords)
    return (ranked_articles[:k]+ranked_articles[-k:], tweets_polarity)


def kwe_process(username, kwe_metric, no):
    
    recommended_articles, tweets_polarity = recommend_articles(username, no, kwe_metric)
    same_polarity = [article for article in recommended_articles if article[1]*tweets_polarity >= 0]
    opposite_polarity = [article for article in recommended_articles if article[1]*tweets_polarity < 0]
    opposite_polarity.reverse()

    lst1_urls = []
    lst1_titles = []
    for article in same_polarity:
        lst1_urls.append(article[0][0])
        lst1_titles.append(article[0][1])

    lst2_urls= []
    lst2_titles = []
    for article in opposite_polarity:
        lst2_urls.append(article[0][0])
        lst2_titles.append(article[0][1])
    
    return lst1_urls, lst1_titles, lst2_urls, lst2_titles
