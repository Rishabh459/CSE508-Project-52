import inputQuerySoup as iq
import loadIISoup as loader

def loadData():
    db = loader.loadII()
    return db

def printTerms(db):
    for i in db.keys():
        print(i, end=", ")

def menu(db):
    printTerms(db)
    print("OP list: NOT, AND, OR, AND NOT, OR NOT")
    print("Enter Query -> format : term1 OP term2 OP term3 ... and so on...")
    pass

def interface(lstOfIDs):
    invertedIndex = loadData()
    i = 0
    while(True):
        i+=1
        # menu(invertedIndex)
        quer = input("Enter the query terms in order here: ")
        if (quer.lower() == 'stop'):
            return 0
        ops = input("Enter the query operations in order here: ")
        userQuery = iq.soupInputQuery(quer, ops)
        # print(invertedIndex['subjected'])
        # break
        userQuerySolution, userQueryNet, userQueryCount = userQuery.runQuery(invertedIndex)
        listOfIDs = [lstOfIDs[i] for i in userQuerySolution]
        print(f"Query {i}", userQueryNet)
        print(f"Number of tweets retrieved for query {i}:", len(userQuerySolution))
        print(f"local ID of tweets retrieved for query {i}:", userQuerySolution)
        print(f"Twitter ID of tweets retrieved for query {i}:", listOfIDs)
        print(f"Number of comparisons required for query {i}:", userQueryCount)


if __name__ == '__main__':
    interface()