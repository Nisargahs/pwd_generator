#nums=[2,3,4,45,5]
#rem_nos=sorted(nums)
#print (rem_nos)
#print(sorted(["hello","abc","aaabb"],reverse=True))#reverse is used for non decreasing order 


#def k(word):
 #   return len(word)

#print(sorted(["zz","aaabb","ytdtyd","aa"],key=k))
def getage(d):
    return d['age']
people=[{"name":"deeksha","age":"20","salary":200000},{"name":"deepika","age":"22","salary":2000000},{"name":"darpak","age":"22","salary":200000}]
print(sorted(people,key=getage))