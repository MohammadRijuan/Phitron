from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def move(self):
        pass

class monkey(animal):
    def __init__(self,name) -> None:
        self.name=name
        self.category='Monkey'


    def eat(self):
        print('m eating banana')
    
    def move(self):
        print('m hanging on the branches')
    
text=monkey('mitu')
text.eat()
text.move()
        