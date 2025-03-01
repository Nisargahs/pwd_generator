citizen=(input("are u citizen of india\n "))
age=int(input('enter your age \n'))
age_above_18= age>=18 
if age_above_18 and citizen=='yes':
    print("you are eligible \n" )
else :
    print("you are not eligible either you are not citizen of india or you are age is below 18 \n")
