from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def formatTextFromFiles(fread, ignoreSet = [], flag = 0):
    # if flag == 1:
    #     print("Preprocessed File :- \n")
    #     print(fread)
    #     print("----------------------")
    punctuations = '''!;:>%^&*()-[]?@#{'"\,<}./$_~'''
    tokens_stop_punct_stripped = []
    tokens_stop_stripped = []
    lines = fread.lower()
    # if flag == 1:
    #     print("----------------------")
    #     print(lines)
    #     print("----------------------")
    tokens = word_tokenize(lines)
    # if flag == 1:
    #     print("----------------------")
    #     print(tokens)
    #     print("----------------------")
    stop_words = set(stopwords.words('english'))

    tokens_stop_stripped = [tok for tok in tokens if ((tok not in stop_words) or (tok in ignoreSet))]
    # if flag == 1:
    #     print("----------------------")
    #     print(tokens_stop_punct_stripped)
    #     print("----------------------")
    tokens_stop_punct_stripped = []

    for tok in tokens_stop_stripped:
        includ = True
        if tok[0] not in punctuations:
            includ = True
        else:
            for ch in tok:
                if ch in punctuations:
                    includ = False
                    break
        if includ:
            tokens_stop_punct_stripped.append(tok)
    # if flag == 1:
    #     print("----------------------")
    #     print(tokens_stop_punct_stripped)
    #     print("----------------------")
    return tokens_stop_punct_stripped

if __name__ == '__main__':
    # print(formatTextFromFiles("infinitely long and simply-supported along"))
    pass