class Student:
    def __init__(self,name,grade,id):
        self.name=name
        self.grade=grade
        self.id=id

    def __repr__(self) -> str:
        return f'Name: {self.name} ,class: {self.grade}, id: {id}'
    

class Teacher:
    def __init__(self,name,subject,id):
        self.name=name
        self.subject=subject
        self.id=id

    def __repr__(self) -> str:
        return f'Name: {self.name}, Subject: {self.subject}, id: {self.id}'
    
class School:
    def __init__(self,name):
        self.name=name
        self.teachers=[]
        self.students=[]

    def add_teacher(self,name,subject):
        id=len(self.teachers)+100
        teacher=Teacher(name,subject,id)
        self.add_teacher.appened(teacher)

    def enroll(self,name,fee,id):
        id=len(self.students)+1
        student=Student(name,grade,id)

