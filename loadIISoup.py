import pickle
def loadII(path="invertedIndexPickled"):
    dataBaseII = open(path, 'rb')	
    II = pickle.load(dataBaseII)
    dataBaseII.close()
    return II


if __name__ == '__main__':
    invertedIndex = loadII()
    print(invertedIndex)