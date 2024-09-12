# Operator overloading refers to the ability to define the behavior of operators such as +, -, *, /, etc., for user-defined classes. In essence, it allows you to use operators with custom types in a way that makes sense for those types. This can lead to more intuitive and readable code.
# Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. This allows subclasses to provide their own behavior for inherited methods.

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def exercise(self):
        return 'lazy ki gym korbo'
    
    def games(self):
        raise NotImplementedError
    
    def study(self):
        return 'study harder'

class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
    
    # override- mane force kortesi person cls er exercise er input ta jno output na ase
    def exercise(self):
        return 'amra strict gym korbo'
    
    def games (self):
        return 'we have to be serious about my game'
    
    # def study(self):
        # pass
    

    # overload
    def __add__(self,other):
        return self.weight + other.weight
    
    def __mul__(self,other):
        return self.age * other.age
    
    def __len__(self):
        return self.height

    
    def __gt__(self,other):
        return self.age > other.age


sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)

print(sakib.exercise())

print(kamal.games())

print(musfiq.study())

print(kamal+jack)

print(kalam*jack)

print(kalam>jack)

print(len(kamal))

