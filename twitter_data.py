# import data from archive folder

import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import formatSoup as ft
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import inputQueryEngineSoup as iq
import buildIISoup as bi
# import data from archive folder
def import_data():
    # get the current working directory
    cwd = os.getcwd()
    # get the path of the archive folder
    archive_path = os.path.join(cwd, 'CSE508_Winter2023_A1_5-main\\archive')
    # get the list of files in the archive folder
    file = os.listdir(archive_path)
    # get the path of the first file in the archive folder
    file_path = os.path.join(archive_path, file[-1])
    # read the csv file
    file = pd.read_csv(file_path)
    # return the dataframe
    return file


def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score
    

if __name__ == '__main__':
    tweetData = import_data()
    tweets = tweetData['tweet']
    tweetIDs = tweetData['id']
    tweetList = []

    for i in tweets:

        lst = " "
        for k in i.split():
            if(k[0] == '@'):
                continue
            lst += k+" "
        tweetList.append(lst)
        tweetList.append(ft.formatTextFromFiles(lst))

    # tweetList has text and emojis with formatting done
    analyser = SentimentIntensityAnalyzer()

    sentimentList = []
    for i in tweetList:
        sentimentList.append(sentiment_analyzer_scores(i))
        # print(i)
        # print(sentiment_analyzer_scores(i))

    # sentimentList has the sentiment scores for each tweet

    tweetsSentID = [tweetIDs, tweetList, sentimentList]

    #builf inverted index
    bi.buildII(tweetsSentID)
    
    query = "search"
    while(query == "search" or query == "Analyse Sentiment"):
        print("You can search or Analyse Sentiment (type 'search' or 'Analyse Sentiment' respectively) or type 'stop' to exit")
        print("Enter your query:", end=" ")

        query = input()
        if query == "search":
            iq.interface(tweetIDs)
        elif query == "Analyse Sentiment":
            print("Enter the local ID you want to analyse sentiment for: ", end=" ")
            i  = int(input().split()[0])
            print("tweet ID: ", tweetIDs[i])
            print(tweetList[i])
            print(sentimentList[i])
        else:
            print("ok, bye!")
            break