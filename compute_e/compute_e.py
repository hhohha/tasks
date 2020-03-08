def compute_e_steps(steps):
    i = 1
    s = 1
    e = 1
    
    while i < steps:
        s *= i
        e += 1/s
        i += 1
            
    return e



def compute_e_steps2(steps):
    i = 1
    s = 1
    e = 1
    
    while i < steps:
        s /= i
        e += s
        i += 1
            
    return e



#print (compute_e_steps(7))


def compute_e_precision(precision):
    i = 1
    s = 1
    currentE = 1
    previousE = 0
    
    while currentE - previousE > precision:
        previousE = currentE
        s *= i
        currentE += 1/s
        i += 1
        
    return currentE

print (compute_e_precision(0.01))
