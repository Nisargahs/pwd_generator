'''
def add(a=20,b=30):
    print(f"sum={a+b}")
add(a,b)
'''

num=int(input("enter num")) 
sum1=1
count=0
i=0
for i in range(1,num):
    while(i!=0):
        sum1=sum1+i%10
        i=i/10
    
    if(sum%2==0):
        count=count+1
    else:
        continue

print(count)