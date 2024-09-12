from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self, name,phone,email,address,money,order) -> None:
        self.wallet=money
        self.__order=order
        self.due_amount=0
        super().__init__(name,phone,email,address)

    @property
    def order(self,order):
        return self.__order
        
    @order.setter
    def order(self,order):
        self.__order=order

    def place_order(self,order):
        self.order=order
        self.due_amount+=order.bill
        print(f'{self.name} placed an order for {order.bill}')

    def eat_food(self,order):
        return f'{self.name} food {order.items}'
    def pay_for_order(self,amount):
        pass

    def give_tips(self,tips_amount):
        pass

    def write_review(self,stars):
        pass

class Employee(User):
    def __init__(self, name,phone,email,address,salary,starting_date,department) -> None:
        super().__init__(name,phone,email,address)
        self.salary=salary
        self.due=salary
        self.department=department
        self.starting_date=starting_date

    def recieve_salary(self):
        self.due=0


class chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department,cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.cooking_item=cooking_item

class server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.tips_earning=0
        super().__init__(name, phone, email, address, salary, starting_date, department)

    def take_order(self,order):
        pass

    def transfer_order(self):
        pass

    def serve_food(self,order):
        pass

    def receieve_tips(self,amount):
        self.tips_earning+=amount

class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)