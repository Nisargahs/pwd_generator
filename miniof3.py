a=int(input("enter the value of a \n"))
b=int(input("enter the value of b \n"))
c=int(input("enter the value of c \n"))
min_of_two= a if a<b else b
min_of_three= min_of_two if min_of_two<c else c
print(f"min of {a}, {b} ,{c} is {min_of_three}")


