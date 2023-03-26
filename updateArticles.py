import os
import json

# open files in the directory each file contains add en extra section in dictionary of the articles with the key as 'article-id' and vallue as the file name+article number
# for example if the file name is 'abc-news.json' and the article number is 1 then the key value pair will be 'article-id':'abc-news/1'
# append this key in the dictionary of each article in the file and update the file with the new dictionary as json
def update():
    for file in os.listdir():
        if len(file.split('_')) > 1:
                continue
        print(file)
        with open(file, 'r') as f:
            data_dict = json.load(f)
        for i in range(len(data_dict['articles'])):
            data_dict['articles'][i]['article-id'] = file.split('.')[0]+'/'+str(i+1)
            f.close()
        with open(file, 'w') as f:
            json.dump(data_dict, f, indent = 4)
            f.close()
        
if __name__ == "__main__":
    update()