class School:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        # composition
        self.classrooms={}
        self.teachers={}

    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom

    def add_teacher(self,subject,teacher):
        self.teachers[subject]=teacher

    def student_admission(self,student):
        className=student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].add_student(student)

        else:
            print(f'There is no classroom like that {className}')

    def __repr__(self) -> str:
        print('----------All Classroom-----------')
        for key, value in self.classrooms.items():
            print(key)
        return ''

class Classroom:
    def __init__(self,name) -> None:
        self.name=name
        self.students=[]
        self.subjects=[]

    def add_student(self,student):
        serial_id=f'{self.name} - {len(self.students) + 1}'
        student.id=serial_id
        self.classroom=self.name #self.name eikane kon cls e seta bujiyece
        self.students.append(student)

    def __str__(self) -> str:
        return f'{self.name} - {len(self.students)}'
    
    def get_top_students(self):
        pass
        
        
        