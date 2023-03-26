import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# make a preprocess function that takes in a string and returns a list of words
def preprocess(text):
    # remove punctuation
    text = re.sub(r'[^\w\s]','',text)
    # make all words lowercase
    text = text.lower()
    # split into a list of words
    text = text.split()
    # remove stopwords
    text = [word for word in text if word not in stopwords.words('english')]
    # remove words with length==1
    text = [word for word in text if len(word)>1]
    # lemmatize words
    lemmatizer = WordNetLemmatizer()
    text = [lemmatizer.lemmatize(word) for word in text]
    return text