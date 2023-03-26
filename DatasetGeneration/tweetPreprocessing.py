import pandas as pd
import numpy as np
import json
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re, string, unicodedata
import nltk
from nltk import word_tokenize, sent_tokenize, FreqDist
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
import generateDataset

# nltk.download
# nltk.download('wordnet')
# nltk.download('stopwords')
from nltk.tokenize import TweetTokenizer
import preprocessor as p

generateDataset.df['hashtag'] = generateDataset.df['Tweet'].apply(lambda x: re.findall(r"#(\w+)", x))
for i, v in enumerate(generateDataset.df['Tweet']):
    # print(i)
    generateDataset.df.loc[i,'text'] = p.clean(str(v))


def preprocess_data(data):
    # Removes Numbers
    data = data.astype(str).str.replace('\d+', '')
    lower_text = data.str.lower()
    lemmatizer = nltk.stem.WordNetLemmatizer()
    w_tokenizer = TweetTokenizer()

    def lemmatize_text(text):
        return [(lemmatizer.lemmatize(w)) for w \
                in w_tokenizer.tokenize((text))]

    def remove_punctuation(words):
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', (word))
            if new_word != '':
                new_words.append(new_word)
        return new_words


    words = lower_text.apply(lemmatize_text)
    words = words.apply(remove_punctuation)
    return pd.DataFrame(words)
pre_tweets = preprocess_data(generateDataset.df['text'])
generateDataset.df['text'] = pre_tweets
stop_words = set(stopwords.words('english'))
generateDataset.df['text'] = generateDataset.df['text'].apply(lambda x: [item for item in \
                                                 x if item not in stop_words])
from ekphrasis.classes.segmenter import Segmenter

# segmenter using the word statistics from Twitter
seg_tw = Segmenter(corpus="twitter")
a = []
print(generateDataset.df.columns)
print(generateDataset.df.head())
for i in range(len(generateDataset.df)):
    # print(generateDataset.df['hashtag'][i])

    if generateDataset.df['hashtag'][i] != a:
        listToStr1 = ' '.join([str(elem) for elem in \
                               generateDataset.df['hashtag'][i]])
        generateDataset.df.loc[i, 'Segmented#'] = seg_tw.segment(listToStr1)
# Frequency of words
fdist = FreqDist(generateDataset.df['Segmented#'])
print(fdist)
print(generateDataset.df.columns)
print(generateDataset.df['hashtag'])
# WordCloud
generateDataset.df.to_csv('LemftData.csv')
# print(generateDataset.df['Segmented#'])
# wc = WordCloud(width=800, height=400, max_words=50).generate_from_frequencies(fdist)
# plt.figure(figsize=(12, 10))
# plt.imshow(wc, interpolation="bilinear")
# plt.axis("off")
# plt.show()
