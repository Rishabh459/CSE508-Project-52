import pickle

def storeII(db, path='invertedIndexPickled'):
	dataBaseII = open(path, 'ab')	
	pickle.dump(db, dataBaseII)					
	dataBaseII.close()
