
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
    
    for pair in argList:
        
        if pair[0] in new_dict:
            new_dict[pair[0]] += pair[1]
        else:
            new_dict[pair[0]] = pair[1]
    #print(new_dict)
            
    return new_dict

def getSortedKeyList(argDict):
    
    new_list = list(argDict.keys())

    new_list.sort()
    #print(new_list)
    return new_list

def computeAverage(newList):
    accum = 0
    avg = 0
    if newList != []:
        for init in newList:
            accum += init
        avg = accum / len(newList)

    return avg


def getSortedListOfTuples(newDict):
    ##new_list = []
    result = newDict.items()
    return sorted(result)
   


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
    
    #firstDict_a = getSortedKeyList(firstDict)
    
    #print(firstDict_a)
    
    #print( key     len(firstDict[key]) computeAverage(firstDict[key])
    
    print ("%20s %5s %10s" %("", "  grade ", ""))
    print ("%20s %5s %10s" %("Name", "  Count ", " Average"))
    print ("-" * 50)

    for init in sorted(firstDict.keys()):
        print("%20s  %5d  %10.2f"%(init, len(firstDict[init]), computeAverage(firstDict[init])) )

    print()
    print ("-" * 50)
    print()
    
    secondDict = getSortedListOfTuples(firstDict)
    
    print ("%20s %5s %10s" %("", "  grade ", ""))
    print ("%20s %5s %10s" %("Name", "  Count ", " Average"))
    print ("-" * 50)

    for init in secondDict:
        a = init[0]
        b = init[1]
        c = computeAverage(init[1])
        print("%20s  %5d  %10.2f"%(a, len(b), c))


















        
    #count = 0

    #for init in firstDict:
        #print(firstDict[init])
        
    #avg_list = []
    #for init in firstDict:
        #compute_avg = computeAverage(firstDict[init])
        #avg_list.append(compute_avg)
    ##print(avg_list)
        
    #keyList= getSortedKeyList(firstDict)
    ##computeAverage(secondDict)
    ##computeAverage(empty_list)
    ##getSortedListOfTuples(thisdict)

    #for index in range(len(grade_list))
    #    len(grade_list[index][1])
        
    #secondList=getSortedListOfTuples(firstDict)




    #values = []
    #key = ''
    
    #for init in secondList:
        #values=computeAverage(init[1])
        #key = init[0]

    
        ##print('%s and %d' %(i[0],computeAverage(i[1])))
    #return value, key
    
main()
