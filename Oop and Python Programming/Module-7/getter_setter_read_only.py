# read only= u cannot set the value and value cannot b changed
# getter = get a vlue of a property..most of the tym u will get the value of a private attribute
# setter= set a value of a property through a method...most of the tym u will set the value of a private property


class user:
    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age=age
        self.__money=money

    def age(self):
        return self._age
    
    # getter without any setter using readonly attribute
    @property
    def agge(self):
        return self._age
    
    def salary(self):
        return self.__money
    
    # getter
    @property
    def salaary(self):
        return self.__money
    
    # setter
    @salaary.setter
    def salaaary(self,value):
        if value < 0:
            return 'value cannot be negative'
        self.__money+=value
    
Student=user('Student', 20, 12000)

# using as a method
print(Student.age())

# now i have used it as attribute by using @property
print(Student.agge)

# used it as a method
print(Student.salary())

# used it as a attribute...when i will used @property it will be getter attribute 
print(Student.salaary)

# by using setter the value can be changed otherwise not...we have to do the function first after that creating another function using previous function name as setter..then it will be updated
Student.salaaary=4000

print(Student.salaaary)