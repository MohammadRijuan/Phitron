import random
from School import*
class Person:
    def __init__(self,name) -> None:
        self.name=name

class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def __repr__(self) -> str:
        return f'{self.name} : {self.subject}'

    def teach(self):
        pass

    
    
    def evaluate_exam(self):
        marks=random.randint(0,100)
        return marks

class Student(Person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        
        self.marks={}
        self.classroom=classroom
        self.__id=None
        self.grade=None
        self.subject_grade={}

    def calculate_final_grade(self):
        sum=0
        for grade in self.subject_grade.values():
            point=School.grade_to_value(grade)
            sum+=point
            print(self.name,grade,point)

        points_avg=sum/len(self.subject_grade)
        self_grade=School.value_to_grade(points_avg)
        print(f'{self.name} {self_grade} with {points_avg}')
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,value):
        self.__id==value
        