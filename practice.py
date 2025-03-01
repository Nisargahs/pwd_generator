"""
def friends( word):
    print('happy new year',word )

friends("emily")
friends("andrew ")
friends("emma")

#friends=['joseph','tom','marcus']
#for names in friends:
#print("happy new year",name)

"""
"""
#summation (method 1 )
a=int(input('enter the number\n' ))
sum=0
for i in range(1,a+1):
    sum=sum+i
print(sum)
"""
"""
#summation method-2
a=int(input('enter the values :\n'))
add=sum
"""
"""
a = int(input("Enter a number:\n")) 
f = 1 
for i in range(1,a+1): 
	f = f * i 
 
print(f'The factorial of the number is {f}') 
"""
"""
a=input("enter the value\n")
print("reverse is", a[::-1])
"""
"""
a=["python","for","coding"]
print("  ".join(a))
"""
"""
#filepath of imported files 
import os 
import socket 
import numpy  
import matplotlib 
import pandas 
print(os)
print(socket)
print(pandas)
print(matplotlib)
print(numpy)
"""
"""
class Myname :
    Ram,Krishna,shankar=range(3)
print(Myname.Ram)
print(Myname.shankar)
"""
"""
text=[1,2,3,4,2,3,2,1,4,4,4,5,6,8,9,8,8,8,8,8]
print(max(set(text),key=text.count))
"""
"""
#memory usage of an object 
import sys 
x=input("enter the value\n")
print(sys.getsizeof(x))
"""
'''
import numpy as np 
arr = np.array([-12,3,9,52,-37,43,-15,63,73,-89,-11,9,-64,93,76,45,53,-14,-43,-68,18,-27,-49,57,88,-92,-36,22,3,9,52,-37,43,-15,63,73,-89,-11,9,-64,93,76,45,53,-14,-43,-68,18,-27,-49,57,88,-92,-36,22,3,9,52,-37,43,-15,63,73,-89,-11,9,-64,93,76,45,53,-14,-43,-68,18,-27,-49,57,88,-92,-36,22,1,-2,-2-2-2,3,4,1,2,3,-3,-4,-4,-5,3,4,1,-3,-2,-2])
arr[arr > 0] = 1
arr[arr < 0] = -1
arr = arr.reshape((10,10))
print(arr)



import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

#generate a random number 
import random 
p= random.randint(0,10)
print(p)


#kilometers to miles 
km=float(input("enter the input\n"))
ml=km*0.6213
print(ml)

cel=float(input("enter the input\n"))
x =(cel * 1.8)+32
print(x)
'''

#to check leap year 
y=int(input("enter the year\n"))
if (y%4==0) and (y%100!=0) or (y%400==0):
    print("its  a leap year")
else:
    print("its not a leap year")