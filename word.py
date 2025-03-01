from snail import *
from plant import *
class World:
    def __init__(self):
        self.days=0

    def simulate(self):
        height =int(input("enter plant height\n"))
        self.plant = Plant(height)
        climb_rate=int(input("enter the snail climb rate\n"))
        slide_rate=int(input("enter the snail slide rate\n"))
        self.plant.putSnail(Snail(climb_rate,slide_rate))

        while True:
            self.days += 1
            self.plant.snail.climb()
            if self.plant.snail.position >= self.plant.height:
                break
            self .plant.snail.slide()

        print(self.days)

World().simulate()

#python supports polymorphism through ducktyping 
