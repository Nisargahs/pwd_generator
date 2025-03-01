s=str(input('enter the string\n'))
part_one=s[1::2]
part_two=s[::2]
res=''
for c1,c2 in zip(part_one,part_two):
    res+=c1+c2
res+= part_two[len(part_one):]
print(res)