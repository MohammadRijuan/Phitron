# base class ,parent class , commom attribute + functionality class

class Gadget:
    def __init__(self,brand,color,price,origin) -> None:
        self.brand=brand
        self.color=color
        self.price=price
        self.origin=origin

    def run(self):
        return f'Running laptop {self.brand}'
    
class laptop:
    def __init__(self,memory,ssd) -> None:
        self.memory=memory
        self.ssd=ssd

    
    def coding(self):
        return f'practicing python at {self.brand}'
    
class Phone(Gadget):
    def __init__(self,sim,number,brand,color,price,origin) -> None:
        self.sim=sim
        self.number=number
        super().__init__(brand,color,price,origin)
    
    def sending_sms(self):
        return f'sending sms to : {self.number}'
    
    def __repr__(self) -> str:
        return f' phone : {self.brand} ,color : {self.color} ,price : {self.price} '
    

class Cameras:
    def __init__(self,lens) -> None:
        self.lens=lens

    def lens(self):
        return f'Changed successful'
    

# common laptop,mpbile,caamera jehetu ek ekta gadget sehetu gadget class call kore common jinisgulo(attribute) class gadget e niye nilam...jemon- brand,price,color run fuction
    
my_phone=Phone('Robi',1833992529,"iphone","Silver",120000,"China")
print(my_phone)

