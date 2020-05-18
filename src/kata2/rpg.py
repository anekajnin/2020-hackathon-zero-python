#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    password = random.choice(string.ascii_letters)
    password = password + random.choice(string.digits)
    password = password + random.choice(string.punctuation)
    #dir
    for n in range(3, passLen):
        option = random.choice(range(3))
        if option == 0:
            password = password + random.choice(string.ascii_letters)
        elif option == 1:
            password = password + random.choice(string.digits)
        else:
            password = password + random.choice(string.punctuation)
        print (password)
    
    passList = list(password)
    random.shuffle(passList)
    password = ''.join(passList)

    return password

print(RandomPasswordGenerator())