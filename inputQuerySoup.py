import loadIISoup as ld
import formatSoup as ft
class soupInputQuery:
    operations = ['AND', 'ANDNOT', 'OR', 'ORNOT']
    def __init__(self, terms="", ops=""):
        self.query = ""
        self.allTerms = []
        self.terms = terms
        self.ops = ops
        self.solution = []
        self.count = 0

    def buildQuery(self):
        for i in range(0, len(self.terms)-1, 2):
            self.query += self.terms[i] + " " + self.ops[i//2] + " " + self.terms[i+1] + " "
        

    def refactor(self):
        # self.allTerms = self.query.split()
        bools = ['and', 'or', 'not']
        self.terms = ft.formatTextFromFiles(self.terms)
        self.ops = ft.formatTextFromFiles(self.ops, bools)
        # print(self.ops, self.terms)
        # if self.ops[0].upper() == 'NOT' and len(self.ops)>1:
        #     a = self.terms[0]
            # self.terms = [a] + self.terms
        i = 0
        print(self.ops, self.terms)
        while(i < len(self.ops)):
            self.ops[i] = self.ops[i].upper()
            if len(self.ops)>i+1 and self.ops[i] == 'AND' and self.ops[i+1].upper() == 'NOT':
                self.ops[i] = "ANDNOT"
                print("pp")
                if(len(self.ops)>i+2):
                    self.ops = self.ops[:i+1:] + self.ops[i+2::]
            elif len(self.ops)>i+1 and self.ops[i] == 'OR' and self.ops[i+1].upper() == 'NOT':
                self.ops[i] = "ORNOT"
                print("gg")
                if(len(self.ops)>i+2):
                    self.ops = self.ops[:i+1:] + self.ops[i+2::]            
            i+=1
        print(self.ops)

        self.buildQuery()
        print(self.query)
            
    def andMerge(self, e1 ,e2 , db):
        self_pointer, other_pointer = 0, 0
        l1 = []
        if (isinstance(e1, list)):
            l1 = e1
        else:
            l1 = db[e1]      
        l2 = []
        if (isinstance(e2, list)):
            l2 = e2
        else:
            l2 = db[e2]      
        result = []
        while(self_pointer < len(l1) and other_pointer < len(l2)):
            self.count+=1
            if l1[self_pointer] == l2[other_pointer]:
                result.append(l1[self_pointer])
                self_pointer += 1
                other_pointer += 1
            elif int(l1[self_pointer]) > int(l2[other_pointer]):
                other_pointer += 1
            elif int(l1[self_pointer]) < int(l2[other_pointer]):
                self_pointer+=1
        return result

    def orMerge(self, e1 ,e2 , db):
        self_pointer, other_pointer = 0, 0
        l1 = []
        if (isinstance(e1, list)):
            l1 = e1
        else:
            l1 = db[e1]
        l2 = []
        if (isinstance(e2, list)):
            l2 = e2
        else:
            l2 = db[e2]      

        result = []
        # print(l1)
        # print(l2)
        while(self_pointer < len(l1) and other_pointer < len(l2)):
            self.count+=1
            if l1[self_pointer] == l2[other_pointer]:
                result.append(l1[self_pointer])
                self_pointer += 1
                other_pointer += 1
            elif int(l1[self_pointer]) > int(l2[other_pointer]):
                result.append(l2[other_pointer])
                other_pointer += 1
            elif int(l1[self_pointer]) < int(l2[other_pointer]):
                result.append(l1[self_pointer])
                self_pointer+=1
        if (len(l1) >= self_pointer):
            result.extend(l1[self_pointer::])
        if (len(l2) >= other_pointer):
            result.extend(l2[other_pointer::])
        print(len(result))
        return result

    def andnotMerge(self, e1 ,e2 , db):
        self_pointer, other_pointer = 0, 0
        l1 = []
        if (isinstance(e1, list)):
            l1 = e1
        else:
            l1 = db[e1]      
        l2 = []
        if (isinstance(e2, list)):
            l2 = e2
        else:
            l2 = db[e2]      

        result = []
        # print(l1/)
        # print(l2)
        while(self_pointer < len(l1) and other_pointer < len(l2)):
            self.count+=1
            if l1[self_pointer] == l2[other_pointer]:
                self_pointer += 1
                other_pointer += 1
            elif int(l1[self_pointer]) > int(l2[other_pointer]):
                other_pointer += 1
            elif int(l1[self_pointer]) < int(l2[other_pointer]):
                result.append(l1[self_pointer])
                self_pointer+=1
        if (len(l1)>=self_pointer):
            result.extend(l1[self_pointer::])
        return result


    def orNotMerge(self, e1, e2, db):
        l2 = []
        if (isinstance(e2) == list):
            l2 = e2
        else:
            l2 = db[e2]
        # l2 = db[e2]
        u = self.universalList(l2)
        print(u)
        return self.orMerge(e1, u)
        

    def revamp(self, i):
        s = str(i)
        return "0"*(4-len(s))+s

    def universalList(self):
        l = []
        for i in range(1400):
            l.append("cranfield"+ self.revamp(i+1))
        return l

    def notMerge(self, e1 ,e2 , db):
        S = self.universalList()
        result = self.andnotMerge(S, e2, db)
        return result

    def resolution(self, db):
        if len(self.terms) == 1:
            if (isinstance(self.terms[0], list)):
                return self.terms[0]
        first = self.terms[0]
        second = self.terms[1]
        oper = self.ops[0]
        result = []
        if (oper == 'AND'):
            result = self.andMerge(first, second, db)
        
        elif (oper == 'OR'):
            result = self.orMerge(first, second, db)    
        
        elif (oper == 'ANDNOT'):
            result = self.andnotMerge(first, second, db)
        
        elif (oper == 'ORNOT'):       
            result = self.notMerge(second, second, db)     
        
        elif (oper == 'NOT'):
            result = self.notMerge(first, second, db)

        self.ops = self.ops[1::]
        self.terms = [result] + self.terms[2::]
        
        return self.resolution(db)


    def runQuery(self, db):
        self.refactor()
        self.solution = self.resolution(db)
        self.terms = []
        self.ops = []
        return (self.solution, self.query, self.count)


if __name__ == '__main__':

    sQ = soupInputQuery("slab is , . a subjected", " or, not   ," )
    print(sQ.runQuery(ld.loadII()))