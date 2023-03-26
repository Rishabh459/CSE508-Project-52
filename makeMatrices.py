import numpy as np
from tqdm import tqdm
import math
# create the tf-idf matrix for each document and 
# Weighting Scheme TF Weight
# Binary 0,1
# Raw count f(t,d)
# Term frequency f(t,d)/Pf(t‘, d)
# Log normalization log(1+f(t,d))
# Double normalization 0.5+0.5*(f(t,d)/ max(f(t‘,d))

def create_tf_idf_matrix_binary(no_of_docs, tf_dict, idf_dict):
    vocab_size = len(idf_dict)
    tf_idf_matrix = np.zeros((no_of_docs, vocab_size))
    # check for all terms in the idf_dict, if it is present in the tf_dict of the document, then set the value to 1*idf
    for i, filename in enumerate(tqdm(tf_dict.keys())):
        for j, token in enumerate(idf_dict):
            if token in tf_dict[filename]:
                tf_idf_matrix[i][j] = 1*idf_dict[token]
                
    return tf_idf_matrix

def create_tf_idf_matrix_raw_count(no_of_docs, tf_dict, idf_dict):
    vocab_size = len(idf_dict)
    tf_idf_matrix = np.zeros((no_of_docs, vocab_size))
    for i, filename in enumerate(tqdm(tf_dict.keys())):
        for j, token in enumerate(idf_dict):
            if token in tf_dict[filename]:
                tf_idf_matrix[i][j] = tf_dict[filename][token]*idf_dict[token]
                
    return tf_idf_matrix

def create_tf_idf_matrix_term_frequency(no_of_docs, tf_dict, idf_dict):
    vocab_size = len(idf_dict)
    tf_idf_matrix = np.zeros((no_of_docs, vocab_size))
    for i, filename in enumerate(tqdm(tf_dict.keys())):
        for j, token in enumerate(idf_dict):
            if token in tf_dict[filename]:
                tf_idf_matrix[i][j] = (tf_dict[filename][token]/len(tf_dict[filename]))*idf_dict[token]

    return tf_idf_matrix

def create_tf_idf_matrix_log_normalization(no_of_docs, tf_dict, idf_dict):
    vocab_size = len(idf_dict)
    tf_idf_matrix = np.zeros((no_of_docs, vocab_size))
    for i, filename in enumerate(tqdm(tf_dict.keys())):
        for j, token in enumerate(idf_dict):
            if token in tf_dict[filename]:
                tf_idf_matrix[i][j] = math.log(1+tf_dict[filename][token])*idf_dict[token]
    
    return tf_idf_matrix

def create_tf_idf_matrix_double_normalization(no_of_docs, tf_dict, idf_dict):
    vocab_size = len(idf_dict)
    tf_idf_matrix = np.zeros((no_of_docs, vocab_size))
    for i, filename in enumerate(tqdm(tf_dict.keys())):
        max_tf = 0
        for token in tf_dict[filename]:
            if tf_dict[filename][token] > max_tf:
                max_tf = tf_dict[filename][token]
        for j, token in enumerate(idf_dict):
            if token in tf_dict[filename]:
                tf_idf_matrix[i][j] = 0.5+0.5*(tf_dict[filename][token]/max_tf)*idf_dict[token]
    return tf_idf_matrix