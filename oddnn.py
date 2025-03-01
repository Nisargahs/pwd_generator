a=input("enter the value of a \n")
a=int(a)

rem = a & 1
print( f'a {a} is {"even" if rem==0 else "odd"}')
