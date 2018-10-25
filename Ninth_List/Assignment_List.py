
'''
ANALYSIS

RESTATEMENT:

  Write a complete program that, given a literal list of tuples,
  prints out a table showing the number of scores and score average in two ways
  
OUTPUT to monitor:

 Table - showing the number of scores and score average

GIVEN:

  

PROCESSING:

  Use the list given in the main function
  

FORMULAS:

  To get an average:
    sum of the values / the number of the values
'''

def tupleListToDict(argList):
    new_dict = {}
    count = 0
    
    new_list = []
    contain_list = []
    
    for i in argList:
        count = argList.index(i) + 1
        if i[0] == argList[count][0]:
            contain_list = i[1] + argList[count][1]
            new_dict[i[0]] = contain_list
    print(new_dict)
            
    return new_dict

def getSortedKeyList(argDict):
    
    new_list = []
    for init in argDict:
        new_list.append(init)

    new_list.sort()
    print(new_list)
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
    
    print(avg)
    return avg


def getSortedListOfTuples(newDict):
    ##new_list = []
    result = newDict.items()
    value = 0
    key = ''
    
    for i in result:
        value = computeAverage(i[1])
        key = i[0]
    
        ##print('%s and %d' %(i[0],computeAverage(i[1])))
    return value, key


def main():
    
    grade_list = [ ('Zaphod', [33, 20]), ('Zaphod', [75, 48]),

      ('Slartibartfast',[]), ('Trillian', [98, 88]), ('Trillian', [97, 77]),

      ('Slartibartfast', []), ('Marvin', [2000, 500]) , ('Arthur', [42, 20]),

      ('Arthur', [64]), ('Trillian', [99]), ('Marvin', [450]),

      ('Marvin', [550]), ('Agrajag', []), ('Agrajag', []), ('Agrajag', [0]),

      ('Ford',[50]), ('Ford', [50]), ('Ford', [50]) ]

    ##thisdict = {"brand": [1,2,3], "model": [3,4,5],"year": [1,9,6,4]}

    ##thislist=[2,3,4,5]

    ##empty_list = []
        
    firstDict=tupleListToDict(grade_list)

    avg_list = []
    for init in firstDict:
        compute_avg = computeAverage(firstDict[init])
        avg_list.append(compute_avg)
    print(avg_list)
        
    ##keyList= getSortedKeyList(firstDict)
    ##computeAverage(secondDict)
    ##computeAverage(empty_list)
    ##getSortedListOfTuples(thisdict)
    
main()
