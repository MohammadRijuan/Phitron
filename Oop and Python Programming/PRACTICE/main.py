from schol_management import*
from persons import*

def main():
    school=School('NMC MODEL HIGH SCHOOL','Chandgaon')
    
    # add classroom
    eight=Classroom('eight')
    school.add_classroom(eight)
    nine=Classroom('nine')
    school.add_classroom(nine)
    ten=Classroom('ten')
    school.add_classroom(ten)

    # add student
    Rijuan=Student("Rijuan",eight)
    school.student_admission(Rijuan)
    print(school)

    physics=Subjectr






if __name__=='__main__':
    main()