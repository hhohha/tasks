from random import random


def get_plain_word():
    f = open('words', 'r')
    words = f.readlines()
    
    f.close()
    return words[int(random() * len(words))][:-1]
    
def get_hidden_word(word):
    hiddenWord = ['_'] * len(word)
    return hiddenWord        



plainWord = get_plain_word()
hiddenWord = get_hidden_word(plainWord)



print ('plainWord:', plainWord)

guesses = 0
while '_' in hiddenWord:
    
    letter = input ('enter a letter\n')
    guesses += 1 
    i = 0
    while i < len(plainWord):
        if plainWord[i] == letter:
            hiddenWord[i] = letter
        i += 1
    
    
    for c in hiddenWord:
        print (c, end=' ')
    print()

print (guesses)
