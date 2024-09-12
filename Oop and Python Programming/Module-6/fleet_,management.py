class company:
    def __init__(self,name):
        self.name=name
        self.buses=[]
        self.routes=[]
        self.drivers=[]
        self.counters=[]
        self.managers=[]
        self.supervisors=[]
    
    def add_bus(self,bus):
        self.buses.append(bus)

    def add_route(self,route):
        self.routes.append(route)

    def add_driver(self,driver):
        self.drivers.append(driver)

    def add_counter(self,counter):
        self.counters.append(counter)
        
    def add_manager(self,manager):
        self.managers.append(manager)

    def add_supervisor(self,supervisor):
        self.supervisors.append(supervisor)

class Bus:
    def __init__(self,serial) -> None:
        self.serial=serial

    def __repr__(self) :
        return f'serial at : {self.serial}'
    
class Route:
    def __init__(self,point,to) -> None:
        self.point=point
        self.to=to

    def __repr__(self) -> str:
        return f'from : {self.point} -> to : {self.to}'

class driver:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def __repr__(self) -> str:
        return f'name : {self.name} ,age : {self.age}'
    
class counter:
    def __init__(self,place) -> None:
        self.place=place

    def __repr__(self) -> str:
        return f'Counter place : {self.place} '
    
class supervisors:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def __repr__(self) -> str:
        return f'name : {self.name} ,age : {self.age}'

class manager:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def __repr__(self) -> str:
        return f'name : {self.name} ,age : {self.age}'
    

Company=company("Marsa")

bus=Bus(10)
route=Route("ctg","Dhaka")
Driver=driver("Abul",30)
Counter=counter("Chandgaon")
supervisor=supervisors("Kudddus",35)
Manager=manager("kalam",20)


Company.add_bus(bus)
Company.add_route(route)
Company.add_driver(Driver)
Company.add_counter(Counter)
Company.add_supervisor(supervisor)
Company.add_manager(Manager)


print(Company.name)    

for obj_list in [Company.buses,Company.counters,Company.routes,Company.drivers,Company.managers,Company.supervisors]:
    for obj in obj_list:
        print(obj)