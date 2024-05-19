from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name=name
        self.email=email
        self.__nid=nid
        self.__id=0
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid) -> None:
        # todo
        current_rider=None
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider name : {self.name} and email address : {self.email}')

    def request_rider(self,location,destination):
        if not self.current_rider:
            # todo:
            ride_request=None
            self.ride_request=None
