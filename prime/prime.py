import math

def isPrime (n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
    
def primes (n):
    i = 2
    lst = []
    while i < n:
        if isPrime(i):
            lst.append(i)
        i += 1
    return lst 



def sieve(n):
    lst = [True] * n
    
    lst[0], lst[1] = False, False
    
    i = 2
    while i < math.sqrt(n):
        if lst[i] == True:
            j = i * 2
            while j < n:
                lst[j] = False
                j += i
        i += 1
    
    i = 0
    while i < len(lst):
        if lst[i]:
            print(i)
        i += 1
    
