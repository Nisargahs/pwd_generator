#class Snail:
#    pass

#s=Snail()
#print(type(s))

#s1=Snail()
#s2=Snail()

#class Snail:
 #   def __init__(self):
  #      self.position=0

#s1=Snail()
#s=Snail()

#print(s.position)
#s.position +=10
#print(s.position)
#print(s1.position)
#functions written inside class is called method 
import random 
class Snail:
    def __init__(self,climb_rate,slide_rate):
        self .climb_rate=climb_rate
        self.slide_rate=slide_rate
        self.position=0
    
    def climb(self):
        self.position += self.climb_rate + random.choice([-0.2,0,0.5])

    def slide(self):
        self.position -=self.slide_rate


if __name__ == '__main__': 

   s1=Snail(3,2)
   s1.climb( )
   s1.slide( )
   print(s1.position)

   s2=Snail(5,2)
   s2.climb( )
   s2.slide( )
   print(s2.position)