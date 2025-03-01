def gencounter(word):
    return {letter : word.count(letter) for letter in word}

print(gencounter("anjfefws")) 

#above is example of dictionarycomprehension and it reduces time 
#jason formate is string and python dictionary 
