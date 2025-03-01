i= int(input("enter the roll no\n"))
num_students = 2

while num_students>=0:
    if i%2==0:
        print(f"call student{i} name ")
        print(f"mark attendence  for student{i}\n\n")
    else :
        print(f"mark absent for student {i}\n")
    num_students-=1
    i+=1