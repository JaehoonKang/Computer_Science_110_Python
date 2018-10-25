grade_list = [ ('Zaphod', [33, 20]), ('Zaphod', [75, 48]), ('Slartibartfast',[]),

      ('Trillian', [98, 88]), ('Trillian', [97, 77]), ('Slartibartfast', []),

      ('Marvin', [2000, 500]) , ('Arthur', [42, 20]), ('Arthur', [64]),

      ('Trillian', [99]), ('Marvin', [450]), ('Marvin', [550]),

      ('Agrajag', []), ('Agrajag', []), ('Agrajag', [0]),

      ('Ford',[50]), ('Ford', [50]), ('Ford', [50]) ]

thisdict =	{
  "brand": [1,2,3],
  "model": [3,4,5],
  "year": [1,9,6,4],
  'apple': [1,2]
}

thislist=[2,3,4,5]

empty_list = []

##print(grade_list)

def tupleListToDict(argList):
    new_dict = {}
    count = 0
    #new_list_key = []
    #new_list_value = []
    new_list = []
    a = []
    
    for i in argList:
        count = argList.index(i) + 1
        if i[0] == argList[count][0]:
            a = i[1] + argList[count][1]
            new_dict[i[0]] = a
            ##print(new_dict)
            
    return new_dict

def getSortedKeyList(argDict):
    
    new_list = []
    for init in argDict:
        new_list.append(init)

    new_list.sort()
    ##print(new_list)
    return new_list

def computeAverage(newList):
    accum = 0
    avg = 0
    for init in newList:
        if newList != []:    
            accum += init
            avg = accum / len(newList)
        else:
            avg = 0
    
    ##print(avg)
    return avg

def getSortedListOfTuples(newDict):
    ##new_list = []
    result = newDict.items()
    #value = 0
    #key = ''
    
    for i in result:
        #value = computeAverage(i[1])
        #key = i[0]
    
        print('%s and %d' %(i[0],computeAverage(i[1])))
    #return value, key
    
        
##tupleListToDict(grade_list)
##getSortedKeyList(thisdict)
##computeAverage(thislist)
##computeAverage(empty_list)
getSortedListOfTuples(thisdict)
