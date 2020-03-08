# task 1 - write a function which takes a list as a parameter and returns the list reversed

# task 2 - write a function which takes a list as a parameter and prints every item in the list as many times as is the value of the item, function returns nothing

# task 3 - write a function which takes a list as a parameter and returns the second highest number

def reverseLst (lst):
    lstR = []
    i = len (lst)-1
    while i >= 0:
        lstR.append (lst[i])
        i = i - 1

    return lstR

# in situ
def reverse(lst):
    i = 0
    while i < len(lst) // 2:
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
        i += 1
    return lst

#print (reverse ([1,2,3,4, 5]))


def printParametrs (lst):
    i = 0
    while i < len (lst):
        
        j = lst[i]
        while j > 0:
            print (lst[i])
            j -= 1
            
        i += 1
    

def shn(lst):
    maxN, max2N = None, None
    for n in lst:
        if maxN is None:
            maxN = n
        elif maxN < n:
            maxN, max2N = n, maxN
        elif n < maxN and max2N is None:
            max2N = n
        elif n < maxN and n > max2N:
            max2N = n
    return max2N
        


def secHighestNumber(lst):
    maxN = None
    
    for n in lst:
        if maxN is None or maxN < n:
            maxN = n
    
    secMaxN = None
    for n in lst:
        if n < maxN:
            if secMaxN is None or secMaxN < n:
                secMaxN = n
        
    return secMaxN



print (shn([1,2,3,4,5,3,4,2,9]))

#print (shn([5,4,3,2]))
