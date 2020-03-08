def intersect (lst1, lst2):
    retLst = []
    for item1 in lst1:
        #print ('prvek z prvniho seznamu bude zpracovan', item1)
        for item2 in lst2:
            #print ('prvek z druheho seznamu bude zpracovan', item2)
            if item1 == item2:
                retLst.append (item1)
        #print ('prvek z prvniho seznamu zpracovan', item1)
    return retLst

l1 = [8,2,3,0,9,6]
l2 = [8,3,4,5,7,2]

expected = [8,2,3]
actual = intersect(l1, l2)

if actual == expected:
    print ('test 1 ok')
else:
    print ('test 1 failed')



#for item in lst:
#    print (item)



print('\n------------------------\n')
# test 1
l1 = []
l2 = []
print (intersect (l1,l2))

print('\n------------------------\n')
#test 2
l1 = [1,1,1,1]
l2 = [2,2,2,2]
print (intersect (l1,l2))

print('\n------------------------\n')

#test 3
l1 = [3]
l2 = [3,3,3,3]
print (intersect (l1,l2))
print('\n------------------------\n')

#test 4
l1 = [0]
l2 = [3,3,3,3]
print (intersect (l1,l2))
print('\n------------------------\n')

#test 5
l1 = [5,5,5,5]
l2 = [1]
print (intersect (l1,l2))
print('\n------------------------\n')

#test 6
l1 = [6,6,6,6]
l2 = [6,6,6,6]
print (intersect (l1,l2))
print('\n------------------------\n')

#test 7
l1 = [1,2,3,4]
l2 = [4,3,2,1]
print (intersect (l1,l2))
print('\n------------------------\n')

#test 8
l1 = [10,20,22]
l2 = [9,10,2,2]
print (intersect (l1,l2))
print('\n------------------------\n')

