#from snail import * 
#class Plant :
 #   def __init__(self,height):
  #      self.height=height

   # def putSnail(self,snail):
    #    self.snail=snail

#p1=Plant(50)
# print(p1.height)
#p1.putSnail(Snail(3,2))
#p1.snail.climb()
#p1.snail.slide()
#print(p1.snail.position)




#alternative method 

import snail 

class Plant :
    def __init__(self,height):
        self.height=height

    def putSnail(self,snail):
        self.snail=snail

p1=Plant(50)
print(p1.height)
p1.putSnail(snail.Snail(3,2))
p1.snail.climb()
p1.snail.slide()
print(p1.snail.position)