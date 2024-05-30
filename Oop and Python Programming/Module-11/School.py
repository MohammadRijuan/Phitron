class School:

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        # composition
        self.classrooms = {}
        self.teachers = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        class_name = student.classroom.name
        if class_name in self.classrooms:
            self.classrooms[class_name].add_student(student)
        else:
            print(f'No classroom named {class_name}')

    @staticmethod
    def calculate_grade(marks):
        if 80<= marks <= 100:
            return 'A+'
        elif 70<= marks <= 79:
            return 'A'
        elif 60<= marks < 70:
            return 'A-'
        elif 50<= marks < 60:
            return 'B'
        elif 40<= marks < 50:
            return 'C'
        elif 33<= marks < 40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map={
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.50,
            'D': 2.00,
            'F': 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if 4.5<= value <= 5.0:
            return 'A+'
        elif 3.5<= value < 4.5:
            return 'A'
        elif 3.00<= value < 3.50:
            return 'A-'
        elif 2.50<= value < 3.00:
            return 'B'
        elif 2.00<= value < 2.50:
            return 'C'
        elif 1.00<= value < 2.00:
            return 'D'
        else:
            return 'F'


    def __repr__(self) -> str:
        print('----------All Classroom-----------')
        for key, value in self.classrooms.items():
            print(key)

        print('----------Students--------')

        print('Class 8 students are')
        eight=self.classrooms['eight']
        for student in eight.students:
            print(student.name)
            
        print(len(eight.students))

        nine=self.classrooms['nine']
        print(len(nine.students))
        ten=self.classrooms['ten']
        print(len(ten.students))

        print('--------Subjects---------')
        for subject in eight.subjects:
            print(f'{subject.name} => {subject.teacher.name}')

        print('--------Exam marks---------')
        for student in eight.students:
            for key,value in student.marks.items():
                print(f'{student.name} - {key} = {value} => {student.subject_grade[key]}')
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
    
    def add_subject(self,subject):
        self.subjects.append(subject)

    def take_semester_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)

        # calculate grade
        for student in self.students:
            student.calculate_final_grade()

    
    def get_top_students(self):
        pass

class subject:
    def __init__(self,name,teacher) -> None:
        self.name=name
        self.teacher=teacher
        self.max_marks=100
        self.pass_marks=33

    def exam(self,students):
        for student in students:
            marks=self.teacher.evaluate_exam()
            student.marks[self.name]=marks
            student.subject_grade[self.name]=School.calculate_grade(marks)
        
        
        
        