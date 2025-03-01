def count(s) :
     
    # Count variable
    res = 0
    rep = 0
     
    for i in range(len(s)) :
         
        # Checking character in string
        if (s[i] == i):
            res = res + 1
        if res==2:
            rep=rep+1
            
    return rep
     
     
# Driver code
str= "pool"
print(count(str))