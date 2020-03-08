# fibonacci sequence  0,1,1,2,3,5,8,13,21

# write function which takes number and print this number of item of fibonacci sequence

def fib(n):
    i = 1
    fibonacci = [0,1]
    
    while i < n:
        fibN = fibonacci [i-1] + fibonacci [i]
        fibonacci.append (fibN)
        i += 1
        
    print (fibonacci)
#fib(10)


def fib2(n):
    a, b, cnt = 0, 1, 2
    
    if n > 0:
        print (a)
    if n > 1:
        print (b)
        
    while cnt < n:
        a, b = b, a+b
        cnt += 1
        print(b)
        
#fib(2)

def fib3 (n):
    i = 0
    fibN = 0
    fibonacci = [0,1]
    
    while fibonacci [i] + fibonacci [i+1] < n:
        fibN = fibonacci [i] + fibonacci [i+1]
        fibonacci.append (fibN)
        i += 1
        
    print (fibonacci)

fib3 (10)
