import json
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from makeMatrices import *
from NRecKW import kwe_process

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

def get_query_vector(twitter_id):
    query_vector = []
    last_name = (twitter_id.split(" ")[1].lower())
    qv_name = last_name + '_qv.json'
    with open(qv_name) as f:
        query_vector = json.load(f)
    return query_vector

def helper_1(option, query_vector):
    number_of_docs = 1800
    vocab_size = 16976

    tf_idf_matrix = np.zeros((number_of_docs, vocab_size))
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
    top_10 = np.argsort(similarity_matrix, axis=0)[-(x+9):][::-1]
    top_10 = top_10.reshape(x+9)
    maplink = json.load(open('maplink.json', 'r'))
    lst = []
    for i, (key, value) in enumerate(maplink.items()):
        if i in top_10:
            if((key,value[0], value[1]) not in lst):
                lst.append((key,value[0], value[1]))
    # return top x in lst
    return lst[x:]


def kwe_result(username, kwe_metric, no):
    lst1_url, lst1_title, lst2_url, lst2_title = kwe_process(username, kwe_metric, no)
    return lst1_url, lst1_title, lst2_url, lst2_title