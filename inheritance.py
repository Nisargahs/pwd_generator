class Animal:
    def __init__(self,color,height):
        self.color=color
        self.height=height

class Tiger(Animal):
    def __init__(self,color,height,stripes):
        super.__init__(color,height)
        self.stripes=stripes


f=Tiger( "red",20,10)
print(f.height,t.color,t.stripes)
