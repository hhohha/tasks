
def sortList(lst):
    isListSorted = False
    while not isListSorted:
        i = 0
        isListSorted = True
        while i < len (lst) - 1:
            if lst[i] > lst[i + 1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                isListSorted = False
            i = i + 1
    return lst
            
# test 1            
unsortedLst = [3,4,6,6,3,5]
sortedLst = [3,3,4,5,6,6]
result = sortList(unsortedLst)

#expected = [3,3,4,5,6,6]
#actual = sortList(...

if result == sortedLst:
    print("test 1 ok")
else:
    print("test 1 failed, expected", sortedLst, " but i got ", result)
    

# test 2            
unsortedLst = []
sortedLst = []
result = sortList(unsortedLst)

if result == sortedLst:
    print("test 2 ok")
else:
    print("test 2 failed, expected", sortedLst, " but i got ", result)
    

# test 3
unsortedLst = [1]
sortedLst = [1]
result = sortList(unsortedLst)

if result == sortedLst:
    print("test 3 ok")
else:
    print("test 3 failed, expected", sortedLst, " but i got ", result)

    
# test 4
unsortedLst = [3,3,3,3,3,3]
sortedLst = [3,3,3,3,3,3]
result = sortList(unsortedLst)

if result == sortedLst:
    print("test 4 ok")
else:
    print("test 4 failed, expected", sortedLst, " but i got ", result)
    
