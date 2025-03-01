product=int(input("enter the value of product \n"))
sum=int(input("enter the value of sum \n"))
a=1; b=1; found=False  
x=0 ; y=0

while b<sum and not found :
    a=1
    while a<sum and not found :
        if a+b==sum and a*b == product :
            found=True
            x=a; y=b
        a+=1
    b+=1
print(x,y) if found  else print(" combination not found ")

