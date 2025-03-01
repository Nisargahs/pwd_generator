s=str(input('enter the string\n'))
part_one=s[1::2]
part_two=s[::2]
res=''
for i in range(len(part_one)):
    res+= part_one[i]+part_two[i]
res+= part_two[i+1:]
print(res)