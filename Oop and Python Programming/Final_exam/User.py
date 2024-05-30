from abc import ABC,abstractmethod
class User:
    def __init__(self,name,email,address) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.bank=None

    @abstractmethod
    def create_an_account(self):
        raise NotImplementedError

class Account_Holder(User):
    def __init__(self, name, email, address,account_type) -> None:
        super().__init__(name, email, address)
        self.account_type=account_type
        self.balance=0
        self.loan=0
        self.loan_amount=0
        self.transaction_history=[]
        self.account_number=None

    def create_an_account(self,bank):
        self.users.bank.append(self)

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            self.bank.balance+=amount

            print(f'Your Deposit has been Successful...here it is ur balance : {self.balance}')

        else:
            print('Deposition system has been failed...Please enter bpositive value')

    def withdraw_money(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            self.bank.balance-=amount

            print(f'here is ur withdrawal amount {amount} and here it is ur balance : {self.balance}')
            self.transaction_history.append(f'withdrawn : {amount}')
        
        elif amount > self.balance:
            print('Withdrawal amount exceeded')
        
        elif self.bank.bankrupt:
            print('Sorry, Bank has gone bankrupt.')
        
    def view_balance(self):
        print(f'Here it is your current balance : {self.balance}')

    def transaction_History(self):
        print('-------Transaction history------')
        for history in self.transaction_History:
            print(history)


class Admin(User):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)
    
    def create_an_account(self):
        self.bank.admins.append(self)