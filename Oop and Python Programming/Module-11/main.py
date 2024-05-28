from School import*
from persons import*

def main():

    school=School('NMC','Chandgaon')
    
    eight=Classroom('eight')
    school.add_classroom(eight)

    nine=Classroom('nine')
    school.add_classroom(nine)
    
    ten=Classroom('ten')
    school.add_classroom(ten)

    print(school)


    
if __name__=='__main__':
    main()

