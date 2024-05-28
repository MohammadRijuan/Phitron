import random
class Person:
    def __init__(self,name) -> None:
        self.name=name

class Teacher(Person):
    def __init__(self, name,subject) -> None:
        self.subject=subject
        super().__init__(name)

    def teach(self):
        pass
    
    def take_exam(self,subject,students):
        for student in students:
            marks=random.randint(0,100)

class Student(Person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        
        self.marks={}
        self.grade=None
        self.classroom=classroom
        self.__id=None
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,value):
        self.__id==value
        