#def sum(nos):
 ##  if nos:
 #    return nos[0]+sum(nos[1:])
    
  #  return 0

#print(sum([i for i in range(5)]))

nos=[34,49,50,65]
val=map(lambda x:x+2,nos)
print(val)

for i in val:
    print(i)

print(list(map(lambda x:x+2,nos )))