class Restaurant:
    def __init__(self,name,rent,menu=[]) -> None:
        self.name=name
        self.chef=None
        self.server=None
        self.manager=None
        self.menu=menu
        self.rent=rent
        self.orders=[]
        self.revenue=0
        self.profit=0
        self.expense=0
        self.balance=0

    def add_employee(self,employee_type,employee):
        if employee_type=='chef':
            self.chef=employee

        elif employee_type=='server':
            self.server=employee

        elif employee_type=='manager':
            self.manager=employee

    def add_order(self,order):
        self.orders.append(order)

    def recieve_amount(self,order,amount,customer):
        # print(amount,order.bill)

        if amount >= order.bill :
            self.revenue+=order.bill
            self.balance+=order.bill
            customer.due_amount=0
            return amount- order.bill
        else:
            print('not enough money')
        
    def pay_expense(self,amount,description):
        if amount < self.balance:
            self.expense += amount
            print(f'expense {amount} for {description} ')
        
        else:
            print(f'dont have enough money to pay expenses {amount}')

    def pay_salary(self,employee):
        print(f'paying salary of {employee.name} with salary {employee.salary}')
        if employee.salary < self.balance:
            self.balance-=employee.salary
            self.expense+=employee.salary
            employee.recieve_salary()

    def show_employees(self):
        print('-----Showing Employees')
        if self.chef is not None:
            print(f'chef name: {self.chef.name} with salary :{self.chef.salary}')
        
        if self.manager is not None:
            print(f'manager name: {self.manager.name} with salary :{self.manager.salary}')
        
        if self.server is not None:
            print(f'server name: {self.server.name} with salary :{self.server.salary}')
