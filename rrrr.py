""" 
def fun(num):
    if num<1 :
        return 0 
    elif num%2==0:
        return fun(num-1)
    else :
        return num+fun(num-2)
print(fun(8))

"""
"""  
def fun2( n,r,p  ):
    return (p((1)+(r/100))**n)

A=fun2(10,5,100)
print(A)

"""

n=int(input("enter the input"))
r=int(input("enter the value"))
p=int(input("enter the number"))

A=p((1+(r/100))**n)
print(A)


