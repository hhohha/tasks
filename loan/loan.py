def loan(amount, interest, payment):
    payedTotal = 0
    months = 0
    
    print ('interest:', amount / 100 * 3.0 / 12)
    while amount > 0:
        monthlyInterest = amount / 100 * interest / 12
        
        amount += monthlyInterest
        amount -= payment
        payedTotal += payment
        months += 1
        
    print ('payed total:', payedTotal)
    
    years = months // 12
    months = months % 12
    print ('payed in:', years, 'years and ', months, 'months')
    
    
loan(4000000, 1.7, 14500)
    
