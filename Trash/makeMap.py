import os
import json

# now we create a dictionary with key as the document id and value as along with 
# the link of the article only and no other information and save the whole dict as map.json
def create_map():
    map_dict = {}
    queries = ['crypto', 'tech', 'business', 'spacex', 'tesla', 'politics', 'AI', 'environment', 'youth activism', 'sustainable', 'climate change', 'social justice', 'women rights', 'sports', 'entertainment', 'cricket', 'comedy', 'chess']
    for file in os.listdir():
        if file.split('.')[0] not in queries:
            continue
        with open(file, 'r') as f:
            data_dict = json.load(f)
            for i in range(len(data_dict['articles'])):
                map_dict[data_dict['articles'][i]['article-id']] = data_dict['articles'][i]['url']
    with open('maplink.json', 'w') as f:
        json.dump(map_dict, f, indent = 4)
        f.close()