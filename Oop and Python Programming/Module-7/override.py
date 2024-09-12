class person:
    def __init__(self,name,age,height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def eat(self):
        print( 'vat mangsho polaw etc')
    
    def exercise(self):
        raise NotImplementedError

class cricketer(person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team=team
        super().__init__(name, age, height, weight)
    
    # override
    def eat(self):
        print('vegetables')

    def exercise(self):
        print('strict exercise')
    
    # + sign operator overload
    def __add__(self,other):
        return self.age + other.age
    
    # * sign overload
    def __mul__(self,other):
        return self.age * other.age
    
    # > operator overload
    def __gt__(self,other):
        return self.age > other.age
    
    # height overload
    def __len__(self):
        return self.height

    
sakib=cricketer('sakib',38,68,78,"BD")
# sakib.eat()
# sakib.exercise()
mushfiq=cricketer("Mushi",36,65,65,"BD")

print(10+5)
print("Rijuan"+"Monju")
# normally cls add,mul,gt,len na nile nicher process ta kknoy possible na
print(sakib + mushfiq)
print(sakib * mushfiq)
print(sakib > mushfiq)
print(len(sakib))