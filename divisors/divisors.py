# ask user for a number and print division to primes

inputStr = input('enter number\n')
n = int(inputStr)

while n > 1:
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            n = n // divisor
            print (divisor)
        divisor += 1
        
            
    
