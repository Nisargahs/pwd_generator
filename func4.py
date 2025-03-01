
def gencount( word):
    counter={}
    for letter in word :
        if letter in counter :
            counter[letter]+=1
        else :
            counter[letter]=1

    return counter
print(gencount("nisarga"))

#times=0
#p="football"
#r=p.count('o')
#print(r)
#for letter in p:
 #   times=times+1
#print(times)
#x=((r/times)*100)
#print(x)