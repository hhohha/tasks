#task 1 - write a function that takes a list as a parameter, return the list without duplicates elements - use sorted list

def remove_duplicates(lst):
    lst = sorted(lst)
    
    i = 0
    lstNew = []
    if len(lst) > 0:
        lstNew.append(lst [i])
    
    while i < len (lst) - 1:
        if lst [i+1] > lst [i]:
           lstNew.append (lst [i+1])
        i += 1
    return lstNew

print (remove_duplicates([3,2,1,2,3,2,3,4,3]))



def remove_duplicates_honza(lst):
    lst = sorted(lst)
    lstNew = []
    lastItem = -1
    
    for item in lst:
        if lastItem != item:
            lstNew.append(item)
        lastItem = item
    return lstNew
        
#print (remove_duplicates_honza([-1,3,2,1,2]))


#task 2 - write a function that takes a list as a parameter, return the list without duplicates elements - don't use sorted list
# may need the command 'break'

def removeDupl (lst):
    lst2 = []
    for item1 in lst:
        dupFound = False
        for item2 in lst2:
            if item1 == item2:
                dupFound = True
        if not dupFound:            
            lst2.append (item1)
    print (lst2)

removeDupl ([3,2,1,2,3,2,3,4,3])    
        



#task 3 - write a function that takes a list and returns the middle element if there is odd number of elements, otherwise return the average of the middle two elements

def middleElement (lst):
    if len (lst) % 2 != 0:
        i = len (lst) // 2
        print (lst[i])
    else:
        i = len (lst) // 2
        middleItem = (lst [i] + lst [i-1]) / 2
        print (middleItem)
        
#middleElement ([1,2,3,4,5,6]))
