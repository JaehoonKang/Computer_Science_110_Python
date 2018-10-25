grade_list = [ ('Zaphod', [33, 20]), ('Zaphod', [75, 48]), ('Slartibartfast',[]),

      ('Trillian', [98, 88]), ('Trillian', [97, 77]), ('Slartibartfast', []),

      ('Marvin', [2000, 500]) , ('Arthur', [42, 20]), ('Arthur', [64]),

      ('Trillian', [99]), ('Marvin', [450]), ('Marvin', [550]),

      ('Agrajag', []), ('Agrajag', []), ('Agrajag', [0]),

      ('Ford',[50]), ('Ford', [50]), ('Ford', [50]) ]


##print(grade_list)

def tupleListToDict(argList):
    new_dict = {}
    
    for i in argList:
        new_dict[argList[i][0]] = argList[i][1]
    return new_dict

tupleListToDict(grade_list)
