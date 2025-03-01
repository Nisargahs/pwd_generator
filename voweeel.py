vowel="AEIOUaeiou"
only_vowel=True
a=input("enter the string \n")
for letter in a :

    if letter  not in  vowel :
         only_vowel =False
         break
print("only vowel" if only_vowel else "non vowel present ")