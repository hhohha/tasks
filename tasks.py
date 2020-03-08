# while 3 > 4:
#     print ('neco vytiskni')
# 
# if 2 == 3:
#    print ('')
# else: 
#    print ('')
#
# i = 4
# i = i + 1
# s = 'string'
# l = [1,2,3]
# l[0] = 5
# r = 5 % 2
#
# print (len(l))
# 


l = [5,6,3,7,9,6,5,6,3,4,6,8,9,5,4,3,6,8,8,9]
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

print('\n------------------------\n')
# task 1 - count and print sum of the list


i = 0
count = 0
while i < len (l):
    count = count + l[i]
    i = i + 1
print (count)

print('\n------------------------\n')
# task 2 - count and print average of the list

i = 0
count = 0
while i < len (l):
    count = count + l[i]
    i = i + 1
print (count/len(l))


print('\n------------------------\n')
# task 3 - print the partial sums of the list

i = 0
count = 0
while i < len (l):
    count = count + l[i]
    i = i + 1
print (count)

print('\n------------------------\n')
# task 4 - print the list as words - [five, six, three, ...

i = 0
while i < len (l):
    value = l[i]
    print (words[value])
    i = i + 1

print('\n------------------------\n')

# task 5 - print only the even number from the list

i = 0
while i < len (l):
    if l[i] % 2 == 0:
        print (l[i])
    i = i + 1

print('\n------------------------\n')
# task 6 - print only prime numbers (difficulty: 4)


 
# task 8 - for each item of the list, print the prefix of the list up to the number (difficulty: 3)

# task 9 - print product of all items in the list (difficulty: 1)
i = 0
count = 1
while i < len (l):
    count = count * l[i]
    i = i + 1
print (count)

print('\n------------------------\n')


# task 10 - print highest number in the list (difficulty: 2)
i = 0
highestNumber = 0
while i < len (l):
    if l[i] > highestNumber:
        highestNumber = l[i]
    i = i + 1
print (highestNumber)
print('\n------------------------\n')

# task 11 - print second highest number in the list (difficulty: 4)

# task 12 - print all numbers higher than 7 (difficulty: 1)
i = 0
while  i < len (l):
    if l[i] > 7:
        print (l[i])
    i = i + 1

print('\n------------------------\n')


# task 14 - print each item in the list 10 times (difficulty: 3)

# task 15 - print each item in the list once and the last item twice (difficulty: 3)

# task 16 - sort the list and print it (difficulty: 6)

# task 17 - print how many times is a number followed by the same number (difficulty: 4)

# task 19 - you have two lists - l1 and l2, print items which are in both lists (difficulty: 4)

# task 22 - print the first 10 items in the list  (if there are less items print it whole) (difficulty: 3)



print('\n-- task seven ----------------------\n')

# task 7 - print sum of numbers on even positions, subtract numbers on odd positions (difficulty: 2)
i = 0
count = 0
while i < len (l):
    if i % 2 == 0:
        count = count + l[i]
    else:
        count = count - l[i]
    i = i + 1
print (count)

print('\n-----task 13 -------------------\n')
# task 13 - print the list except the last item (difficulty: 2)
i = 0
while i < len (l)-1:
    print  (l[i])
    i = i + 1
 
 
print('\n--------task 20----------------\n')
# task 20 - print every third number in the list (difficulty: 2)

i = 2
while i < len (l):
    print (l[i])
    i = i + 3


print('\n--------task 21----------------\n')
l = [5,1,6,3,7,9,6,5,6,3,4,6,8,9,5,1,4,3,6,8,1,8,9]
# task 21 - print 'yes' if the list contains number 1 three times, otherwise print 'no' (difficulty: 2)

i = 0
count = 0
while i < len (l):
    if l[i] == 1:
        count = count + 1
    i += 1
if count > 2:
    print ('yes')
else:
    print ('no')
        

