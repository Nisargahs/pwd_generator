ch= input ("enter the character\n")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("it is a vowel")
elif '0'<= ch<= '9':
    print("it is a digit")
elif 'a' <= ch <= 'z':
    print('it is a consonant')
elif ch=="@" or ch=="#" or ch=='$':
    print("it is a special character")
else :
    print("not an alphabet ,not a digit")