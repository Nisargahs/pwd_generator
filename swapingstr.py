s="abcde"
letters=list(s)
for i in range(0,len(s)-1,2):
    letters[i],letters[i+1]=letters[i+1],letters[i]
res=''.join(letters)
print(res)


