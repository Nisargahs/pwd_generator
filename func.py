'''a
=10; b=20
def add( ):
    global a 
    a+=2
    return a+b
print(add())
print("outside",a,b)

def gencount(num):
    counter={}
    for digit in num :
        if digit in counter :
            counter[digit]+=1
        else :
            counter[digit]=1

    return counter
print(gencount("572378233"))


times=0
p=(input())
r=p.count((input()))
print(r)
#for letter in p:
 #   times=times+1
#print(times)


#num=int(input())
def getProduct(n):
 
    product = 1
 
    while (n != 0):
        product = product * (n % 10)
        n = n // 10
 
    return product
 
# Driver Code
n =int(input())
print(getProduct(n))
'''
x=int(input())
y=int(input())
lst=[12,12,34,45,54]

for lst[i] in range(x,y):
    print(i)

 
