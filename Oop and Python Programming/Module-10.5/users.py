from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self,name,email,phone,password) -> None:
        self.name=name
        self.email=email
        self.phone=phone
        self.__password=password

class Customer(User):
    def __init__(self, name, email, phone, password,order,money) -> None:
        self.__order=order
        self.wallet=money
        super().__init__(name, email, phone, password)

    @property
    def order(self,order):
        return self.__order
    
    @order.setter
    def order(self,order):
        self.__order=order

    def place_an_order


    
        
