from abc  import ABC,abstractmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self,company_name) -> None:
        self.company_name=company_name
        self.riders=[]
        self.drivers=[]
        self.rides=[]

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_drivers(self,driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'company anme :{self.company_name} and riders :{len(self.riders)} and drivers : {len(self.drivers)}
                
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
        self.cur_ride=None

    def display_profile(self):
        print(f'rider with name : {self.name} and email : {self.email}')

    def load_cash(self,amount):
        if amount > 0:
            self.wallet+=amount
    
    def update_location(self,current_location):
        self.current_location=current_location


    def request_ride(self,rider_sharing,current_location,destination):
        if not self.cur_ride:
            ride_request=Ride_Request(self,current_location,destination)
            ride_matcher=Ride_matching(rider_sharing.drivers)
            ride=ride_matcher.find_driver(ride_request)
            print('got a ride',ride)
            self.cur_ride=ride
    
    def show_cur_ride(self):
        print(self.cur_ride)


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
class Vehicle(ABC):

    speed={ 'car': 50,
             'Bike':70
    }
    def __init__(self,license_plate,vehicle_type,rate) -> None:
        self.license_plate=license_plate
        self.vehicle_type=vehicle_type
        self.rate=rate
        self.status='Available'
    
    @abstractmethod
    def start_drive(self):
        pass

class car(Vehicle):
    def __init__(self, license_plate, vehicle_type, rate) -> None:
        super().__init__(license_plate, vehicle_type, rate)
        

    def start_drive(self):
        self.status='unavailble'

class Bike(Vehicle):
    def __init__(self, license_plate, vehicle_type, rate) -> None:
        super().__init__(license_plate, vehicle_type, rate)

    def start_drive(self):
        self.status='available'

Ride_sharing=


        
        
        
