import json
# create posting list that has key as the word and value as a list of article-ids in which the word is present and the number of documents in which the word is present
def create_posting_list():
    posting_list = {}
    with open('preprocessed_files.json', 'r') as f:
        preprocessed_dict = json.load(f)
        for key in preprocessed_dict.keys():
            for word in preprocessed_dict[key]:
                if word in posting_list.keys():
                    posting_list[word][0].append(key)
                    posting_list[word][1] += 1
                else:
                    posting_list[word] = [[key], 1]
    with open('posting_list.json', 'w') as f:
        json.dump(posting_list, f, indent = 4)
        f.close()
