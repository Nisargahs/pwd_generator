count={"1":1,"2":5,"3":5,"7":2,"8":7}
num1=int(input("enter the number1\n"))
num2=int(input("enter the number2\n"))
total=num1+num2
print(total)
total=str(total)
match_stick_count=0
for digit in total:
    match_stick_count += count.get(digit,0)


print(match_stick_count)