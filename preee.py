present=0 
absent=0
num_student =3
i=1
while num_student>0:
    status=input(f"calling student{i}\n")
    if status=="P":
        present +=1
    else:
        absent +=1
        break
    num_student -=1
if absent:
    print("class is cancelled ") 
else:
    print(f"present={present}")      

    