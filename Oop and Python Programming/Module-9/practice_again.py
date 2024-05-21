from abc  import ABC,abstractmethod
from datetime import datetime
class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name=name
        self.email=email
        self.__nid=nid
        self.__id=0
        self.wallet=0
    
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid,current_location,initial_amount) -> None:
        super().__init__(name, email, nid)        
        self.current_location=current_location
        self.wallet=initial_amount

    def display_profile(self):
        print(f'rider with name : {self.name} and email : {self.email}')

class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location=current_location
        self.wallet=0

    def display_profile(self):
        print(f'driver name : {self.name} and email : {self.email}')

    def accept_ride(self):
        self.set_driver(self)

class Ride:
    def __init__(self,current_location,end_location) -> None:
        self.current_location=current_location
        self.end_location=end_location
        self.started_time=None
        self.ended_time=None
        self.rider=None
        self.driver=None
        self.estimated_fare=None

    def set_driver(self,driver):
        self.driver=driver

    def start_ride(self,ride):
        self.started_time=datetime.now()

    def end_ride(self,rider,amount):
        self.ended_time=datetime.now()
        self.rider.wallet-=amount
        self.driver.wallet+=amount

class Ride_Request:
    def __init__(self,rider,current_location,destination) -> None:
        self.rider=rider
        self.current_location=current_location
        self.destination=destination

class Ride_matching:
    def __init__(self,driver) -> None:
        self.available_driver=driver

    def find_driver(self):
        if len(self.available_driver) > 0:
            print('looking for a driver')
            driver=self.available_driver[0]
            ride=Ride(Ride_Request.Rider.current_location,Ride_Request.Rider.end_location)
            driver.accept_ride(ride)
            return ride

        
        
