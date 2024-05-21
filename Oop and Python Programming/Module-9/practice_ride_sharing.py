from datetime import datetime
from abc import ABC, abstractmethod

class Ride_Sharing:
    def __init__(self, Company_name) -> None:
        self.company_name = Company_name
        self.riders =[]
        self.drivers =[]
        self.rides = []
    
    def add_riders (self, rider):
        self.riders.append(rider)
    
    def add_drivers(self, driver):
        self.drivers.append(driver)
        
    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}'


    
class User(ABC):
    
    def __init__(self, name, email, Nid) -> None:
        self.name = name 
        self.email = email
        #TODO set user id dynamically
        self.__id = 0
        self.__Nid = Nid
        self.wallet = 0
      
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, Nid, cur_location, initial_amount) -> None:
        self.cur_location = cur_location
        self.wallet = initial_amount
        self.cur_ride = None
        super().__init__(name, email, Nid)
        
    def display_profile(self):
        print(f'Rider -> Name : {self.name} and Email : {self.email}')
   
    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
    
    def update_location(self, cur_location):
        self.cur_location = cur_location

    def request_ride(self, ride_sharing, destination):
        if not self.cur_ride:
            ride_request = Rider_rquest(self, destination)
            ride_mathcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_mathcher.find_drivers(ride_request)
            print("Got The ride .", ride)
            self.cur_ride = ride
            
    def show_cur_ride(self):
        print(self.cur_ride)

class Drivers(User):
    def __init__(self, name, email, Nid, cur_location) -> None:
        super().__init__(name, email, Nid)
        self.cur_location = cur_location
        self.wallet = 0
    
    def display_profile(self):
        print(f'Driver -> name : {self.name} and email : {self.email}')
    
    def accept_ride(self, ride):
        ride.set_driver(self)
        
class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self):
        return f'Ride Details: Started: {self.start_location} to {self.end_location}'
        
        
    
class Rider_rquest:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location
        


class Ride_Matching:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers
    
    def find_drivers(self, rider_request):
        if len(self.available_drivers) > 0:
            print("He is available for drive .")  
            driver = self.available_drivers[0]
            ride = Ride(rider_request.rider.cur_location, rider_request.end_location)
            driver.accept_ride(ride)
            return ride
        
class Vehicle(ABC):
    speed = {
        'car': 50,
        'bike': 70,
        'CNG': 15
    }
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'Available'
    
    @abstractmethod
    def start_drive(self):
        pass
    
class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'Unavailable'
    
class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'Unavailable'

ride_sharing = Ride_Sharing("ABC Ride Sharing")

while True:
    print("Menu: ")
    print("1. Add rider ")
    print("2. Add driver ")
    print("3. print ")
    print("4. Quit ")
    user_input = input("Enter your choice : ")
    
    if user_input == '1':
        # Add rider
        rider_name = input("Enter rider name: ")
        rider_email = input("Enter rider email: ")
        rider_nid = input("Enter rider NID: ")
        rider_location = input("Enter rider current location: ")
        initial_wallet_amount = float(input("Enter initial wallet amount: "))
        
        rider = Rider(rider_name, rider_email, rider_nid, rider_location, initial_wallet_amount)
        ride_sharing.add_riders(rider)
        
    elif user_input == '2':
        # Add driver
        driver_name = input("Enter driver name: ")
        driver_email = input("Enter driver email: ")
        driver_nid = input("Enter driver NID: ")
        driver_location = input("Enter driver current location: ")
        
        driver = Drivers(driver_name, driver_email, driver_nid, driver_location)
        ride_sharing.add_drivers(driver)
        
    elif user_input == '3':
        destination = input("Enter destination: ")
        print(ride_sharing)
        rider.request_ride(ride_sharing,destination)
        rider.show_cur_ride()
    
    elif user_input == '4':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")



