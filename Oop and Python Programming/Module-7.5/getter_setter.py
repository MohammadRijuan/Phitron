class Student:
    def __init__(self, name, age, classes, id) -> None:
        self._name = name
        self._age = age
        self._classes = classes
        self.__id = id
    
    # getter
    @property
    def naame(self):
        return self._name  
    
    def name(self):
        return self._name  
    
    @property
    def agge(self):
        return self._age
      
    def age(self):
        return self._age  
    
    @property
    def classes(self):
        return self._classes  
    
    def claasses(self):
        return self._classes  
    
    @property
    def student_id(self):
        return self.__id
    
    # setter by setting up a value 
    @student_id.setter
    def student_idd(self,value):
        self.__id=value

# Creating an instance of the Student class
Rijuan = Student('Rijuan', 20, 14, 4) 

# Accessing attributes using properties
print(Rijuan.name()) 
print(Rijuan.naame) 
print(Rijuan.age()) 
print(Rijuan.agge) 
print(Rijuan.claasses())
print(Rijuan.classes)

print(Rijuan.student_id)

Rijuan.student_idd=1

print(Rijuan.student_idd)

        