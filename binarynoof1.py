count=0
num=int(input("enter the number \n"))
y=bin(num)
while num:
    count += num&1
    num >>=1
print(count)
print(y)