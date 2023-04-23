import os
import storeIISoup as st
import formatSoup as ft

def buildI():
    dataDir = r'CSE508_Winter2023_Dataset'
    inverted_index = {}
    j = 0
    for file in sorted(os.listdir(dataDir)):
        f = open(dataDir + '/' + file, 'rt')
        fread = f.read()
        if j < 5:
            tokens_stop_punct_stripped = ft.formatTextFromFiles(fread, [], 1)
        else:
            tokens_stop_punct_stripped = ft.formatTextFromFiles(fread)
        f.close()
        filename = file.split('/')[-1]
        for i in tokens_stop_punct_stripped:
            if i not in inverted_index:
                inverted_index[i] = [filename]
            if inverted_index[i][-1] != filename:
                inverted_index[i].append(filename)
        j+=1
    st.storeII(inverted_index)

def buildII(lst):
    inverted_index = {}
    for i in range(len(lst[0])):
        for j in lst[1][i]:
            if j not in inverted_index:
                inverted_index[j] = [i]
            if inverted_index[j][-1] != i:
                inverted_index[j].append(i)
    st.storeII(inverted_index)