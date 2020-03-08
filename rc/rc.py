# task - write function that takes a personal number as a string and verifies its validity
# check that:
#  - it has right lenght
#  - it contains digit
#  - day must not be greater than 31
#  - month must be valid number
#  - the whole number must be divisible by 11


# first try to write functions pn_length and pn_div_by_eleven

def pn_length(n):
    #return len (n) == 10
    
    if len (n) == 10:
        return True
    else:
        return False
    
def pn_digits(n):
    for c in n:
        if c > '9' or c < '0':
            #ASCII tabulka
            return False
    return True

def pn_day(n):
    day= int(n[4] + n[5])
    if day < 32:
        return True
    else:
        return False
    
def pn_month(n):
    month = int (n[2] + n[3])
    if month < 13 or (month < 63 and month > 50): 
        return True
    else:
        return False
    
def pn_div_by_eleven(n):
    # here you will need the function int() to make a number out of the string, you will also need the operator modulo - %
    pn = int (n)
    if pn % 11 == 0:
        return True
    else:
        return False
    
def validatePN(n):
    if pn_length(n) and pn_digits(n) and pn_day(n) and pn_month(n) and pn_div_by_eleven(n):
        return True
    else:
        return False

# test
print (validatePN('8560104289'))
