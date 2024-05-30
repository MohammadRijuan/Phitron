class School:

    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.students={}
        self.classrooms={}
        self.teachers={}

    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom        
    
    def add_teacher(self,teacher,subject):
        self.teachers[subject]=teacher

    def student_admission(self,student):
        class_name=student.classroom.name

        if student in self.classrooms:
            self.classrooms[class_name].add_student(student)

        else:
            print(f'no class named {class_name}')

        
    def __repr__(self) -> str:
        print( f'    {self.name}')
        print('----------All Classroom-----------')
        for key, value in self.classrooms.items():
            print(key)

        eight=self.classrooms['eight']
        for student in eight.students:
            print(student.name)

        return ''

        

class Classroom:
    def __init__(self,name) -> None:
        self.name=name
        self.subjects=[]
        self.students=[]

    def __repr__(self) -> str:
        return f'{self.name} : {len(self.students)}'

    def add_student(self,student):
        serial_id=f'{self.name} - {len(self.students)} + 1 '
        id=serial_id
        self.classroom=self.name
        self.students.append(student)    

    def add_subject(self,subject):
        self.subjects.append(subject)    