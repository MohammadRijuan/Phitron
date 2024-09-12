from School import*
from persons import*

def main():

    school=School('NMC','Chandgaon')

    # Add classroom
    eight=Classroom('eight')
    school.add_classroom(eight)

    nine=Classroom('nine')
    school.add_classroom(nine)
    
    ten=Classroom('ten')
    school.add_classroom(ten)

    #Add students 
    Rijuan=Student('Rijuan',eight)
    school.student_admission(Rijuan)
    
    Monju=Student('Monju',eight)
    school.student_admission(Monju)
    
    Sifat=Student('Sifat',nine)
    school.student_admission(Sifat)

    # subjects
    physics_teacher=Teacher('Nurul islam')
    physics=subject('Physics',physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher=Teacher('Ayub sir')
    chemistry=subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)
    
    math_teacher=Teacher('kamal sir')
    math=subject('math',math_teacher)
    eight.add_subject(math)


    eight.take_semester_exam()


    print(school)


    
if __name__=='__main__':
    main()

