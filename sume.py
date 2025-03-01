s=input("enter the string\n")
total=0

for letter in s:

    if '0' <= letter <='9':
        total += int(letter)
print(total) 