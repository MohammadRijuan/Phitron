import random
import datetime
from bank import*

class User:

    Accounts=[]
    total_loan=0
    total_balance=0

    def __init__(self,name,email,address,account_type) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.bank=None
        self.account_number=self.random_account_number()
        self.account_type=account_type
        self.balance=0
        self.loan=True
        self.total_loan=0
        self.amount_of_loan=0
        self.transaction_history=[]
        self.bankrupt=False
        self.account_number=None
        User.Accounts.append(self)


    def random_account_number(self):
        return "".join(str(random.randint(0, 9)) for i in range(2))

class Account_Holder(User):
    def __init__(self, name, email, address,account_type) -> None:
        super().__init__(name, email, address,account_type)

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            User.total_balance+=amount

            print(f'Your Deposit has been Successful...here it is ur balance : {self.balance}')
            self.transaction_history.append(f'deposit : {amount}')

        else:
            print('Deposition system has been failed...Please enter bpositive value')

    def withdraw_money(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            # self.bank.balance-=amount

            print(f'here is ur withdrawal amount {amount} and here it is ur balance : {self.balance}')
            self.transaction_history.append(f'withdrawn : {amount}')
        
        elif amount > self.balance:
            print('Withdrawal amount exceeded')
        
        elif self.bank.bankrupt:
            print('Sorry, Bank has gone bankrupt.')

    def getting_loan(self,money):
        if self.loan==True:
            if money >= self.balance:
                print('loan exceeded')
            
            elif money<=0:
                print('please provide non negative number')

            else:
                self.balance+=money
                self.total_loan+=1
                self.amount_of_loan+=money
                User.total_loan+=money
                User.total_balance-=money
                print(f'successfully u have got a loan {money}..your balance is {self.balance}')
                self.transaction_history.append(f'loan : {money}')

        else:
            print('sorry,we cannot give you any loan')

    def show_amount_of_loan(self):
        print(f'Total loan u have taken : {self.amount_of_loan}')

    def transfer_balance(self, name, amount):
        if self.transfer_permit:
            if amount > 0:
                if self.balance >= amount:
                    receiver = next((user for user in User.Accounts if isinstance(user, Account_Holder) and user.name == name), None)
                    if receiver:
                        receiver.deposit(amount)
                        self.balance -= amount
                        self.transaction_history.append((amount, receiver.name, datetime.now()))
                        print(f'{amount} Tk transferred from account {self.name} to account {receiver.name} successfully')
                    else:
                        print('Receiver not found!')
                else:
                    print('you dont have enough balance')
            else:
                print('Transfer a valid amount')
        else:
            print('Transfer system is not working')

        
    def view_balance(self):
        print(f'Here it is your current balance : {self.balance}')

    def show_transaction_history(self):
        print('-------Transaction history------')
        for history in self.transaction_history:
            print(history)


class Admin(User):
    def __init__(self, name, email, address,password) -> None:
        super().__init__(name, email, address,'current')
        self.password=password
    
    def create_an_account(self,name,email,address,account_type):
        user=Account_Holder(name,email,address,account_type)
        print('Created the account successfully')
        print(f'Account name : {name} , email : {email} ,account_type: {user.account_number}')

    def view_users(self):
        print('-------Users------')
        for user in User.Accounts:
            if isinstance(user,Account_Holder):

                print(f'Name: {user.name} Email: {user.email} Balance: {user.balance} Account number: {user.account_number} loan amount: {user.amount_of_loan}')
        
        print('End of the list')

    def delete_a_user(self,account_name):
        for user in User.Accounts:
            if isinstance(user, User) and user.name == account_name:
                User.Accounts.remove(user)
                print(f'Successfully delete the user.')
                return
        print(f'User not found')


    def total_bank_balance(self):
        print(f'The total bank balance is : {User.total_balance}')

    def show_total_loan(self):
        print(f'Bank total loan is : {User.total_loan}')

    def loan_feature(self,loans):
        if not loans:
            for user in User.Accounts:
                if isinstance(user,Account_Holder):
                    user.loan=False
            print('currently loan feature is off')

        else:
            for user in User.Accounts:
                if isinstance(user,Account_Holder):
                    user.loan=True
            print('loan feature is on') 

    def bankruptt(self,bankrupttt):
        if bankrupttt:
            for user in User.Accounts:
                if isinstance(user, Account_Holder):
                    user.bankrupt = True
            print(f'Bankrupt')
        else:
            for user in User.Accounts:
                if isinstance(user, Account_Holder):
                    user.bankrupt = False
            print(f'Bank is not bankrupt anymore') 

      


    