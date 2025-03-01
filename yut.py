''' 
#divisibility test  5 and 7 present in the given range 
n=int(input())
for i in range(1,n+1):
    if i%5==0 or i%7==0:
        print(i,end=' ')


#given number is perfect or not (if the summation of the factors of given number is equal to that number)
n=int(input())
s=0
for i in range(1,n):
    if (n%i==0):
        s+=i
if(n==s):
    print("it is perfect number")
else:
    print("it is not a perfect number")


n=int(input())
if (n==1):
    print(0)
if(n==2):
    print(1)
if(n==3):
    print(2)
else:
    if n%2==1:
        print('3')

    else:
        print(2)


list1=[1,2,3,2,3,2,3,3,4,5,6,5,6]
list2=sort.list1()
print(list2)

#remove characters with even index
s=input("enter the string\n")
s1=''
for i in range(0,len(s)):
    if i%2!=0:
        s1+=s[i]
print(s1)

str=input("enter line of string\n")
rep=input("enter char to replace\n")
for i in str:
    if i in "aeiouAEIOU":
        print(rep,end="")
    else:
        print(i,end="")
        
str=input("enter line of string\n")
rep=input("enter char to replace\n")
res=""
for i in str:
    if i in "aeiouAEIOU":
        res=res+rep
    else:
        res=res+i
print(res)

#lower case first upper case next 
str1=str(input("enter the string\n"))
lower=[]
upper=[]
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

result=''.join(lower+upper)
print(result)


#count number of digits,alphabets and special characters 
str1 = "P@#yn26at^&i5ve"
digits =0
alphabets=0
special=0
for char in str1:
    if char.isalpha():
        alphabets+=1
    elif char.isdigit():
        digits+=1
    else:
        special+=1
print("Digits=",digits, "alphabets=",alphabets ,"special=",special)


#string balancing
def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "iasw"
s2 = "Nisarga"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

'''
