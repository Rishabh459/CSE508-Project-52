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

def helper_1(option, query_vector):
    # create_tf()
    # create_idf_dict(number_of_docs, posting_list)

    # vocab_size = len(json.load(open('idf.json', 'r')))
    # number_of_docs = len(json.load(open('preprocessed_files.json', 'r')))
    number_of_docs = 1800
    vocab_size = 16976

    tf_idf_matrix = np.zeros((number_of_docs, vocab_size))

    # if option == 'Jaccard Coefficient'
    if option == "Binary Weighting Scheme":
        tf_idf_matrix = create_tf_idf_matrix_binary(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
    
    elif option == "Raw Count Weighting Scheme":
        tf_idf_matrix = create_tf_idf_matrix_raw_count(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))

    
    elif option == "Term Frequency Weighting Scheme":
        tf_idf_matrix = create_tf_idf_matrix_term_frequency(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
        
    elif option == "Log Normalization Weighting Scheme":
        tf_idf_matrix = create_tf_idf_matrix_log_normalization(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))
       
    elif option == "Double Normalization Weighting Scheme":
        tf_idf_matrix = create_tf_idf_matrix_double_normalization(number_of_docs, json.load(open('tf.json', 'r')), json.load(open('idf.json', 'r')))    

    similarity_matrix = cosine_similarity(tf_idf_matrix, [query_vector])

    return similarity_matrix

# recommend top x articles
def recommend_top_10_articles(similarity_matrix, x):
    top_10 = np.argsort(similarity_matrix, axis=0)[-x:][::-1]
    top_10 = top_10.reshape(x)
    maplink = json.load(open('maplink.json', 'r'))
    lst = []
    for i, (key, value) in enumerate(maplink.items()):
        if i in top_10:
            lst.append((key,value[0], value[1]))
    return lst

# binary_top_10 = recommend_top_10_articles(double_normalization_similarity_matrix)