vowels="aeiouAEIOU"
count=0
s=input("enter the string\n ")
i=0
while i<len(s):
    c=s[i]
    count+=1 if c in vowels else 0
    i+=1
print(count)
