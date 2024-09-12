class Student:
    def __init__(self, name, grade, id):
        self.name = name
        self.grade = grade
        self.id = id

    def __repr__(self) -> str:
        return f'Name: {self.name}, class: {self.grade}, id: {self.id}'


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Name: {self.name}, Subject: {self.subject}, id: {self.id}'


class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 100
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, grade, fee):
        if fee < 6500:
            return "You cannot buy the course"
        else:
            id = len(self.students) + 1
            student = Student(name, grade, id)
            self.students.append(student)

    def print_info(self):
        print(f"School: {self.name}")
        print("Teachers:")
        for teacher in self.teachers:
            print(teacher)
        print("Students:")
        for student in self.students:
            print(student)


phitron = School('Phitron')
phitron.enroll('Rijuan', 12, 6500)
phitron.enroll('Monju', 13, 4500)
phitron.enroll('Md', 10, 7000)

phitron.add_teacher('Nibraj', 'chem')
phitron.add_teacher('tohid', 'math')
phitron.add_teacher('fahad', 'js')

phitron.print_info()



class Shop:
    shopping_mall = 'Jamuna'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


