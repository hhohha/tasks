
#f = open('f1', 'r')
#data = f.readlines()
#f.close()

#print (data)



#f = open('f1', 'r')

#d = []
#for line in f:
    #d.append(line)

#print(d)
#f.close()




#f = open('f2', 'w')
#f.write('abcdefgh')
#print ('writing finished')
#f.close()


#f = open('f2', 'a')
#f.write('abcdefgh')
#print ('writing finished')
#f.close()



# otevri soubor f1, spocitej vsechny znaky v souboru a jejich pocet zapis do souboru f2


f = open('f1', 'r')
data = f.readlines()
count = 0
for string in data:
    for item in string:
        count += 1
    
print (count)
countW = str (count) 
 
d = open('f2', 'w')
d.write (countW)
d.close()

f.close()
