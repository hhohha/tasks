#task 1 - write a function that takes a string and returns number of words in the string (words are always divided by the space character)
def numberOfWords (s):
    i = 0
    space = ' '
    words = 1
    while i < len (s):
        if s[i] == space:
            words += 1
        i += 1
    return words

#print (numberOfWords('a b c'))

#task 2 - write a function that takes a string and turns it into a list
def stringIntoList (s):
    lst = []
    for char in s:
        lst.append(char)
    return lst
#print (stringIntoList ('asdfrewq'))

#task 3 - write a function that takes a string and finds out if it is a palindrom (string that is read the same from the start and from the end), return True or False
def IsItPalindrom (stri):
    strBackward = ''
    i = len (stri) - 1
    while i >= 0:
        strBackward += stri[i]
        i -= 1
    
    return stri == strBackward
    
    #if stri == strBackward:
        #return True
    #else:
        #return False
        
print (IsItPalindrom ('123321'))
