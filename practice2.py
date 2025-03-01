'''
a=[11,2,3,4,5,32,4,6,775,56,90,6,7,75]
a.sort()
print(a)
print(a[0])

string = "picture perfect";  
freq = [None] * len(string);  
for i in range(0, len(string)):  
    freq[i] = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j]):  
            freq[i] = freq[i] + 1;  
               
            string = string[ : j] + '0' + string[j+1 : ];   
for i in range(0, len(freq)):  
    if(string[i] != ' ' and string[i] != '0'):  
        print(string[i] + "-" + str(freq[i]));  
'''
