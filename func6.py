#def square(nos):
 #   return [i**2 for i in nos ]
#print(square([23,34,4,56]))


#def squarev1(nos):
 #   for num in nos:
  #      yield num**2#generator ref

#print(squarev1([23,434,545]))

#g=squarev1([23,434,545,4,56])

#print(next(g))
#rint(next(g))
#print(next(g))
#print(next(g))

#for val in squarev1([23,434,545,4,56]):
 #   print(val)

def  squarev2(nos):
    return (num**2 for num in nos)    
for val in squarev2([23,434,545,4,56]):
   print(val)
