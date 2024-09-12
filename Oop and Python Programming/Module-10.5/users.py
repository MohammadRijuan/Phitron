from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self,name,email,phone,password) -> None:
        self.name=name
        self.email=email
        # self.phone=phone
        self.__password=password

    



    
        