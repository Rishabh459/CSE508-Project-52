
import pandas as pd
from preprocess import *
import json
def storeUsers(users):
    dir = 'News Articles/'
    for i in users:        
        tweet_data = pd.read_csv(dir + i+'_Data.csv')
        # print(number_of_docs)
        # pick up the columnn text and convert it to a list
        tweet = tweet_data['Tweet'].tolist()

        # append all the tweeets space seperated to make a paragraph
        paragraph = ' '.join(tweet)

        tweet_corpus = preprocess(paragraph)

        # idf_dict is the vocabulary vector create a query vector such that if the word is present in the query, then set the value to 1, where query vector is tweet_cotpus
        idf_dict = json.load(open(dir+'idf.json', 'r'))
        query_vector = []
        for token in idf_dict:
            if token in tweet_corpus:
                query_vector.append(1)
            else:
                query_vector.append(0)

        # store query vector as a json file
        with open(dir +i+'_qv.json', 'w') as f:
            json.dump(query_vector, f)

        
if __name__ == '__main__':
    users = ['kohli', 'greta', 'samay', 'pichai']
    storeUsers(users)
