def novaFunkce(x, y):
    return x*y


a = novaFunkce(3, 6)  
print (a)

# task 1 - write function that takes one numeric parameter and computes its factorial (2)  ex.: factorial(5) == 5*4*3*2*1
# task 2 - write function that takes two numeric parameters and returns smaller number (1)
# task 3 - function takes one numeric parameter - circle radius(polomer kruhu) - and computes surface (2)
# task 4 - write function that takes two params - list of numbers and a number and returns boolean (logicka hodnota) - true if the sum of the list is equal to the number, else false (2)
# task 5 - function takes a number and prints all even numbers which are smaller (2)
# task 6 - write a function that takes one numeric parameter and prints out if it is positive or negative or zero (1)
# task 7 - write function that takes two parameters - string (retezec) and character(znak) and returns index of the first occurence(vyskytu) of the character in the string (3)

print ('\n------two-------\n')
def smallerNumber (x, y):
    if x > y:
        return y
    else:
        return x

print (smallerNumber(6, 12))    



print ('\n------six-------\n')
def allParametrs (x):
    if x > 0:
        print ('positive')
    elif x == 0:
        print ('zero')
    else:
        print ('negative')

allParametrs (9)



print ('\n------one-------\n')

def factorial (x):
    count = 1
    while x > 0:
        count = count * x
        x = x - 1
    return count
    
print (factorial (5))

print ('\n------three-------\n')
def circleSurface (x):
    return x*x*3.14

print (circleSurface(2))

#ukazka
def isListEmpty(lst, x):
    if len(lst) == 0:
        print ('it is empty')
    else:
        print ('it is not empty')
    
isListEmpty ([1,2,3], 0)

print ('\n-------------\n')
