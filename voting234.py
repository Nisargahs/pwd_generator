citizen=(input("are u citizen of india\n "))
age=int(input('enter your age \n'))
age_above_18= age>=18 
if age_above_18 and citizen=='yes':
    print("you are eligible \n" )
elif  not age_above_18 :
    print(" age is not above 18 ")
else:
    print("you are not a citizen") 
    