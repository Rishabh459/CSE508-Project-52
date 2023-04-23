import os
import nltk

# import nltk libraries for preprocessing
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import json
import math

os.chdir('News Articles')
nltk.download('wordnet')
# create a dictionary for term frequency that has key as the article-id and value as a dictionary with key as the word and value as the frequency of the word in the article
def create_tf():
    tf_dict = {}
    with open('preprocessed_files.json', 'r') as f:
        preprocessed_dict = json.load(f)
        for key in preprocessed_dict.keys():
            tf_dict[key] = {}
            for word in preprocessed_dict[key]:
                if word in tf_dict[key].keys():
                    tf_dict[key][word] += 1
                else:
                    tf_dict[key][word] = 1
    with open('tf.json', 'w') as f:
        json.dump(tf_dict, f, indent = 4)
        f.close()


# create idf dict
def create_idf_dict(no_of_docs, posting_list):
    idf_dict = {}
    for token in posting_list:
        idf_dict[token] = math.log(no_of_docs / posting_list[token][1]+1)
    with open('idf.json', 'w') as f:
        json.dump(idf_dict, f, indent = 4)
        f.close()