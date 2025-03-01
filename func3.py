

def anagram (s1,s2):
    if len(s1)!=len(s2):
        return False
    for c in s1:
        if c in s2:
            s2=delete (s2,c)
        else: 
            return False
    return  True  

def delete(s,c):
    for i in range(len(s)):
        if s[i]==c:
            break
    return s[:i]+s[i+1:]

print(anagram("abcd","bac"))
