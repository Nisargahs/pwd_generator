class Animal:
    def grow(self):
        print("animal grows")

class Tiger(Animal):
    count=0
    def __init__(self,age):
        self.age = age

    def __add__(self,other):
        return self.age + other.age

#t1=Tiger(10)
#t2=Tiger(10)
#print(t1+t2)

Tiger.count=20
t.count=20
print(t1.count)