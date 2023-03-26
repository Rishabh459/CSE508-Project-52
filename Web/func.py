import json
import numpy as np
import pandas as pd
import json
import pandas as pd
import numpy as np
# from makeMatrices import *
# from preprocess import *
from sklearn.metrics.pairwise import cosine_similarity

from makeMatrices import *
# from makePostings import *
# from makeTfidf import *
# import pickle
# from updateArticles import *
# from preprocess import *
# from makeMap import *
# from preprocessArticles import *


user_data = []

def add_new_user(bname, bemail, btwitterid):
    bname = bname.lower()
    user_data.append([bname, bemail, btwitterid])
    print(user_data)

def get_user_data(sname, stwitterid):
    for i in range(len(user_data)):
        sname = sname.lower()
        if user_data[i][0] == sname and user_data[i][2] == stwitterid:
            return user_data[i]
        else:
            return -1

def get_news_articles(stwitterid):
    with open('business.json', 'r') as f:
        business = json.load(f)['articles']

    url_list = []
    article_title = []
    out_list = []
    for i in range(len(business)):
        article_title.append(business[i]['title'])
        url_list.append(business[i]['url'])
    
    # store a list in a list
    for i in range(len(article_title)):
        out_list.append([article_title[i], url_list[i]])

    for j in range(len(article_title)):
        out_list.append([article_title[i], url_list[i]])

    return out_list


def get_query_vector(twitter_id):
    query_vector = []
    last_name = (twitter_id.split(" ")[1].lower())
    qv_name = last_name + '_qv.json'
    with open(qv_name) as f:
        query_vector = json.load(f)
    return query_vector

def helper_1():
    number_of_docs = len(json.load(open('preprocessed_files.json', 'r')))
    # create_tf()
    # create_idf_dict(number_of_docs, posting_list)

    binary_tf_idf_matrix = create_tf_idf_matrix_binary(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
    raw_count_tf_idf_matrix = create_tf_idf_matrix_raw_count(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
    term_frequency_tf_idf_matrix = create_tf_idf_matrix_term_frequency(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
    log_normalization_tf_idf_matrix = create_tf_idf_matrix_log_normalization(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
    double_normalization_tf_idf_matrix = create_tf_idf_matrix_double_normalization(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
    return binary_tf_idf_matrix, raw_count_tf_idf_matrix, term_frequency_tf_idf_matrix, log_normalization_tf_idf_matrix, double_normalization_tf_idf_matrix

