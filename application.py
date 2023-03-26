import json
import pandas as pd
import numpy as np
from makeMatrices import *
from preprocess import *
from sklearn.metrics.pairwise import cosine_similarity
from makePostings import *
from makeTfidf import *
import pickle
from updateArticles import *
from preprocess import *
from makeMap import *
from preprocessArticles import *

# update()
# preprocess_articles()
# create_map()
# create_posting_list()

posting_list = json.load(open('posting_list.json', 'r'))
number_of_docs = len(json.load(open('preprocessed_files.json', 'r')))
# create_tf()
# create_idf_dict(number_of_docs, posting_list)

binary_tf_idf_matrix = create_tf_idf_matrix_binary(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
raw_count_tf_idf_matrix = create_tf_idf_matrix_raw_count(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
term_frequency_tf_idf_matrix = create_tf_idf_matrix_term_frequency(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
log_normalization_tf_idf_matrix = create_tf_idf_matrix_log_normalization(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
double_normalization_tf_idf_matrix = create_tf_idf_matrix_double_normalization(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))

# # save the similarity matrix in a pickle file
# with open('binary_tf_idf_matrix.pkl', 'wb') as f:
#     pickle.dump(binary_tf_idf_matrix, f)
# with open('raw_count_tf_idf_matrix.pkl', 'wb') as f:
#     pickle.dump(raw_count_tf_idf_matrix, f)
# with open('term_frequency_tf_idf_matrix.pkl', 'wb') as f:
#     pickle.dump(term_frequency_tf_idf_matrix, f)
# with open('log_normalization_tf_idf_matrix.pkl', 'wb') as f:
#     pickle.dump(log_normalization_tf_idf_matrix, f)
# with open('double_normalization_tf_idf_matrix.pkl', 'wb') as f:
#     pickle.dump(double_normalization_tf_idf_matrix, f)


tweet_data = pd.read_csv('kohli_Data.csv')
# print(number_of_docs)
# pick up the columnn text and convert it to a list
tweet = tweet_data['Tweet'].tolist()

# append all the tweeets space seperated to make a paragraph
paragraph = ' '.join(tweet)

tweet_corpus = preprocess(paragraph)

# idf_dict is the vocabulary vector create a query vector such that if the word is present in the query, then set the value to 1, where query vector is tweet_cotpus
idf_dict = json.load(open('idf.json', 'r'))
query_vector = []
for token in idf_dict:
    if token in tweet_corpus:
        query_vector.append(1)
    else:
        query_vector.append(0)

# create a similarity matrix for the query vector and the tf-idf matrix
# binary_tf_idf_matrix = pickle.load(open('binary_tf_idf_matrix.pkl', 'rb'))
# raw_count_tf_idf_matrix = pickle.load(open('raw_count_tf_idf_matrix.pkl', 'rb'))
# term_frequency_tf_idf_matrix = pickle.load(open('term_frequency_tf_idf_matrix.pkl', 'rb'))
# log_normalization_tf_idf_matrix = pickle.load(open('log_normalization_tf_idf_matrix.pkl', 'rb'))
# double_normalization_tf_idf_matrix = pickle.load(open('double_normalization_tf_idf_matrix.pkl', 'rb'))

binary_similarity_matrix = cosine_similarity(binary_tf_idf_matrix, [query_vector])
raw_count_similarity_matrix = cosine_similarity(raw_count_tf_idf_matrix, [query_vector])
term_frequency_similarity_matrix = cosine_similarity(term_frequency_tf_idf_matrix, [query_vector])
log_normalization_similarity_matrix = cosine_similarity(log_normalization_tf_idf_matrix, [query_vector])
double_normalization_similarity_matrix = cosine_similarity(double_normalization_tf_idf_matrix, [query_vector])
x = 6
# recommend top x articles
def recommend_top_10_articles(similarity_matrix):
    top_10 = np.argsort(similarity_matrix, axis=0)[-x:][::-1]
    top_10 = top_10.reshape(x)
    return top_10

binary_top_10 = recommend_top_10_articles(double_normalization_similarity_matrix)

# recommend top 50 articles
# def recommend_top_50_articles(similarity_matrix):
#     top_50 = np.argsort(similarity_matrix, axis=0)[-50:][::-1]
#     top_50 = top_50.reshape(50)
#     return top_50

# binary_top_10 = recommend_top_50_articles(double_normalization_similarity_matrix)

# use the maplink.json to recommend top 10 news artiles
maplink = json.load(open('maplink.json', 'r'))
for i, (key, value) in enumerate(maplink.items()):
    if i in binary_top_10:
        print(key)
        print(value)

