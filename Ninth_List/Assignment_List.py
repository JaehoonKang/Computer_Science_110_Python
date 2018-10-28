'''
ANALYSIS

RESTATEMENT:

  Write a complete program that, given a literal list of tuples,
  prints out a table showing the number of scores and score average in 2 ways
  
OUTPUT to monitor:

 Two Tables - showing name, the number of scores, and score average

    The first table: Using three funtions and list from a given dictionary
    The second table: Using a funtion and tuple from a given dictionary

GIVEN:


PROCESSING:

  Use the list (tuples inside) given in the main function
  
  Define and use four functions
      tupleLisToDict() is converting List to Dictionary

      getSortedKeyList() is sorting out keys in a list

      computeAverage() is computing an average value in a list

      getSortedListOfTuple() is getting all the keys from a dictionary 

  Use a given list with tuples inside and convert it to dictionary

  Using the dictionary converted, for the first part, with getSortedKeyList()
      Create a table for name, count, and average

  Using the dictionary converted, for 2 part, with getSortedListofTuples()
      Create a table with anme, count, and average
  
FORMULAS:

  To get an average:
    sum of the values / the number of the values
'''
# Define tupleListToDict function to convert List to Dictionary
def tupleListToDict(argList):
    # Create a new dictionary workingas a accumulator
    new_dict = {}

    # Using for loop to iterate through list
    for pair in argList:

        # For each tuple, put it in an empty dictionary
        # if the key is already in the dictionary
        # concatenate the values 
        if pair[0] in new_dict:
            new_dict[pair[0]] += pair[1]

        # else, just put it in the dictionary
        else:
            new_dict[pair[0]] = pair[1]
            
    ##Debugging created List
    ##print(new_dict)
            
    return new_dict

# Define getSortedKeyList function to sort out keys in a list
def getSortedKeyList(argDict):

    # Using keys() method to get keys from a dictionary
    new_list = list(argDict.keys())

    # Using sort() method, sorting out the list
    new_list.sort()
    #print(new_list)
    return new_list

# Define computeAverage funciton
def computeAverage(newList):
    # Create accumulators: accum, avg
    accum = 0
    avg = 0

    #Branch: if newList is not empty
    if newList != []:

        # Using for loop to iterate newList
        for init in newList:
            accum += init

        # Using accum (accumulator) & len function to get avg (average)
        avg = accum / len(newList)
        
    ##Debugging
    ##print(avg)
    return avg


# Define getSortedListOfTuples to get all the keys from a dictionary 
def getSortedListOfTuples(newDict):
    
    result = newDict.items()

    ##Debugging result items
    ##print(result)

    ##return sorted result
    return sorted(result)
   


def main():

    grade_list = [ ('Zaphod', [33, 20]), ('Zaphod', [75, 48]),

      ('Slartibartfast',[]), ('Trillian', [98, 88]), ('Trillian', [97, 77]),

      ('Slartibartfast', []), ('Marvin', [2000, 500]) , ('Arthur', [42, 20]),

      ('Arthur', [64]), ('Trillian', [99]), ('Marvin', [450]),

      ('Marvin', [550]), ('Agrajag', []), ('Agrajag', []), ('Agrajag', [0]),

      ('Ford',[50]), ('Ford', [50]), ('Ford', [50]) ]

    fruit_list = [ ('Apple', [33, 20, 45]), ('Apple', [75, 48, 69]),

      ('Kiwi',[]), ('Banana', [98, 88]), ('Banana', [97, 77]),

      ('Kiwi', []), ('Pineapple', [2000, 500]) , ('Pineapple', [42, 20]),

      ('Pineapple', [64]), ('Watermelon', [99]), ('Watermelon', [450]),

      ('Peanut', [550]), ('Peanut', []), ('Peanut', [12, 32]), ('Peanut', [0]),

      ('Strawberry',[50]), ('Strawberry', [50]), ('Strawberry', [50]) ]
    
    ##Debugging samples
    
    ##thisdict = {"brand": [1,2,3], "model": [3,4,5],"year": [1,9,6,4]}

    ##thislist=[2,3,4,5]

    ##empty_list = []


    # The outcome after tupleListToDict()    
    firstDict=tupleListToDict(grade_list)

    #Using format specifiers, create a table
    
    print ("%20s %5s %10s" %("", "  grade ", ""))
    print ("%20s %5s %10s" %("Name", "  Count ", " Average"))
    print ("-" * 50)

    # Using sorted(), sorting dictionary using getSortedKeyList()
    for init in getSortedKeyList(firstDict):
        print("%20s  %5d  %10.2f"\
              %(init, len(firstDict[init]), computeAverage(firstDict[init])))

    print()
    print ("-" * 50)
    print()

    # For the second part, using a tuple
    secondList = getSortedListOfTuples(firstDict)

    # Using format specifiers, create a table for the second part
    print ("%20s %5s %10s" %("", "  grade ", ""))
    print ("%20s %5s %10s" %("Name", "  Count ", " Average"))
    print ("-" * 50)

    # For loop to iterate through the list
    for init in secondList:

        # Save each assigned values to relevant variable names
        name = init[0]
        count = init[1]
        average = computeAverage(init[1])

        # Print out the outcome using formate specifiers
        print("%20s  %5d  %10.2f"%(name, len(count), average))

    print()
    print()
    print()
    print("Second Test Run with Fruits")
    print("-" * 60)
    print()
    print()


    # The outcome after tupleListToDict()    
    secondDict=tupleListToDict(fruit_list)

    #Using format specifiers, create a table
    
    print ("%20s %5s %10s" %("", "  grade ", ""))
    print ("%20s %5s %10s" %("Name", "  Count ", " Average"))
    print ("-" * 50)

    # Using sorted(), sorting dictionary using getSortedKeyList()
    for init in getSortedKeyList(secondDict):
        print("%20s  %5d  %10.2f"\
              %(init, len(secondDict[init]), computeAverage(secondDict[init])))

    print()
    print ("-" * 50)
    print()

    # For the second part, using a tuple
    secondList = getSortedListOfTuples(secondDict)

    # Using format specifiers, create a table for the second part
    print ("%20s %5s %10s" %("", "  grade ", ""))
    print ("%20s %5s %10s" %("Name", "  Count ", " Average"))
    print ("-" * 50)

    # For loop to iterate through the list
    for init in secondList:

        # Save each assigned values to relevant variable names
        name = init[0]
        count = init[1]
        average = computeAverage(init[1])

        # Print out the outcome using formate specifiers
        print("%20s  %5d  %10.2f"%(name, len(count), average))

main()
