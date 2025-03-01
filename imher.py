class Animal:
    def grow(self):
        print("animal grows")

class Tiger(Animal):
    pass
    def grow(self):
        print("tiger grows")
    def __repr__(self):
        return "i am tiger"

    

t=Tiger()
t.grow()
print(t)


t1=Tiger()
t2=Tiger()
print(t1+t2)