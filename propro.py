'''
    dice simulator program 
import random 
while True :
    print(' 1. roll the dice            2.exit     ')
    user = int(input("what you want to do\n'"))
    if user==1:
        number = random.randint(1,6)
        print(number)
    else:
        break
'''

#random password generator 

import random 
passlen = int(input("enter the length of the password\n"))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
p= "".join(random.sample(s,passlen ))
print(p)