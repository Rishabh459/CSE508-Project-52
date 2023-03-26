import os
import json

# now we preprocess the text in each article and store it in a dictionary with key as the article-id and value as the list of words
# send the author title description and content of each article to the preprocess function and store the list of words in a dictionary
# with key as the article-id and value as the list of words in a new file called 'filename_preprocessed.json'
def preprocess_articles():
    preprocessed_dict = {}
    for file in os.listdir():
        print(file)
        with open(file, 'r') as f:
            if len(file.split('_')) > 1:
                continue
            data_dict = json.load(f)
            for i in range(len(data_dict['articles'])):
                # only preprocess article section that are not empty
                preprocessed_dict[data_dict['articles'][i]['article-id']] = []
                if data_dict['articles'][i]['content'] != None:
                    preprocessed_dict[data_dict['articles'][i]['article-id']].extend(preprocess(data_dict['articles'][i]['content']))
                if data_dict['articles'][i]['title'] != None:
                    preprocessed_dict[data_dict['articles'][i]['article-id']].extend(preprocess(data_dict['articles'][i]['title']))
                if data_dict['articles'][i]['description'] != None:
                    preprocessed_dict[data_dict['articles'][i]['article-id']].extend(preprocess(data_dict['articles'][i]['description']))
                if data_dict['articles'][i]['author'] != None:
                    preprocessed_dict[data_dict['articles'][i]['article-id']].extend(preprocess(data_dict['articles'][i]['author']))
            f.close()
    with open('preprocessed_files.json', 'w') as f:
        json.dump(preprocessed_dict, f, indent = 4)
        f.close()