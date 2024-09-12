from math import pi

class shape:
    def __init__(self,name) -> None:
        self.name=name

class rectangle(shape):
    def __init__(self, name,length,width) -> None:
        self.length=length
        self.width=width
        super().__init__(name)

    def area(self):
        return f' rectangular area is : {self.length * self.width}'
    
class circle(shape):
    def __init__(self, name,radius) -> None:
        self.radius=radius
        super().__init__(name)

    def area(self):
        return f'circle area is :{ pi * self.radius*self.radius}'
    
ayothoketro=rectangle('ayothokethro',2,3)
print(ayothoketro.area())

britto=circle('britto',2)
print(britto.area())