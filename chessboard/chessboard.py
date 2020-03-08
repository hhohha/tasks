# task 1 - function takes two coordinates of two rooks on a chessboard, returns true or false if the rooks can take each other
# we supposse that chessboard has size 8 x 8 (coordinates cannot be grater than 8)
# we supposse that the two coordinates are different from each other

def rooks(l1, l2):
    if l1[0] == l2[0] or l1[1] == l2[1]:
       return True
    else:
        return False
    
# exaple of function call
# first coordinate is column, second id row

#print (rooks([2,4], [5,6]))


# task 2 - do the same with queens
def queens(l1, l2):
    if rooks(l1, l2):
        return True
    
    if l1[0] - l2[0] == l1[1] - l2[1]:
        return True
    
    if l1[0] - l2[0] == l2[1] - l1[1]:
        return True
    
    return False

# task 3 - test function queens

#print (queens([2,4],[5,6]))
#print (queens([2,4],[2,8]))
#print (queens([2,1],[8,7]))
#print (queens([1,8],[8,1]))
#print (queens([1,7],[7,1]))



# task 4 - write function kings
def kings (l1,l2):
    if (l1[0] == l2[0] or l1[0] == l2[0]+1 or l1[0] == l2[0]-1) and (l1[1] == l2[1] or l1[1] == l2[1]+1 or l1[1] == l2[1]-1):
        return True
    else:
        return False
    
def kings2(l1,l2):
    return abs(l1[0] - l2[0]) <= 1 and abs(l1[1] - l2[1]) <= 1

#print (kings ([3,3],[3,8]))

# task 5 - write function knights (jezdec / kun)
def knights (l1,l2):
    if l1[0] == l2[0]-2 and l1[1] == l2[1]+1:
        return True
    if l1[0] == l2[0]-1 and l1[1] == l2[1]+2:
        return True
    if l1[0] == l2[0]-2 and l1[1] == l2[1]-1:
        return True
    if l1[0] == l2[0]-1 and l1[1] == l2[1]-2:
        return True
    
    if l1[0] == l2[0]+2 and l1[1] == l2[1]+1:
        return True
    if l1[0] == l2[0]+1 and l1[1] == l2[1]+2:
        return True
    if l1[0] == l2[0]+2 and l1[1] == l2[1]-1:
        return True
    if l1[0] == l2[0]+1 and l1[1] == l2[1]-2:
        return True
    
    else:
        return False
  
def knights2(l1, l2):
    return abs(l1[0] - l2[0]) + abs(l1[1] - l2[1]) == 3 and not rooks(l1,l2) 

#print (knights ([3,3],[3,8]))
#print (knights ([3,3],[2,5]))
