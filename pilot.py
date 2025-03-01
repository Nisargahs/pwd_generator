#def  greet( name):
 #   return f"hello{name}"
#msg=greet("nisarga")
#print(msg)

#num=20
#def inc(num):
 #   num+=1
  #  return num
#res=inc(20)
#print(res,num)

#num=20
#def inc():
#   global num 
#   num+=10
#   print(num)
  
#res=inc()
#inc(res,num)


num=20
def inc(num):
    num+=10 
    print(f"inside{num}")

inc(num)
print(f"outside {num}")