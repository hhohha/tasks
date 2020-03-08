#task - write function that takes 1 number as a parameter and translates it into a roman number

def roman_numbers(n):
    letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    retLst = []
    
    i = 0
    while n > 0:
        lastDigit = n % 10
        n = n // 10
                
        if lastDigit == 0:
            pass
        elif lastDigit == 1:
            retLst.append(letters[i])
        elif lastDigit == 2:
            retLst.append(letters[i])
            retLst.append(letters[i])
        elif lastDigit == 3:
            retLst.append(letters[i])
            retLst.append(letters[i])
            retLst.append(letters[i])
        elif lastDigit == 4:            
            retLst.append(letters[i+1])
            retLst.append(letters[i])
        elif lastDigit == 5:
            retLst.append(letters[i+1])
        elif lastDigit == 6:
            retLst.append(letters[i])
            retLst.append(letters[i+1])
        elif lastDigit == 7:
            retLst.append(letters[i])
            retLst.append(letters[i])
            retLst.append(letters[i+1])
        elif lastDigit == 8:
            retLst.append(letters[i])
            retLst.append(letters[i])
            retLst.append(letters[i])
            retLst.append(letters[i+1])
        elif lastDigit == 9:
            retLst.append(letters[i+2])
            retLst.append(letters[i])
        i += 2
        
    retLst.reverse()
        
    return retLst
    
print (roman_numbers(5555))
