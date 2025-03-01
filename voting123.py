citizen=(input("are u citizen of india\n "))
age=int(input('enter your age \n'))
age_above_18= age>=18 
if age_above_18 :
    if citizen=='y':
        print("you are eligible \n")
    else:
        print("not a citizen")
else:
    if citizen=='y'  :
        print("age<18,not eligible")  
    else:
        print("age<18,not a citizen,not eligible")   