import random

class Bank:
    def __init__(self,name) -> None:
        self.name=name

    def __repr__(self) -> str:
        return f'welcome to {self.name}\n'
        


class Account_holder:
    Accounts=[]
    toatl_balance=0
    total_loan_amount=0

    def __init__(self,name,email,address,phone,account_type) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.phone=phone
        self.account_type=account_type
        self.account_number=self.random_account_number()
        self.balance=0
        self.number_of_loan=0
        self.amount_of_loan=0
        self.transcation_history=[]
        self.permission_of_loan=True
        self.bankrupt=False
        self.permission_of_transfer=True
        Account_holder.Accounts.append(self)

    def random_account_number(self):
        return ''.join(random.choices('0123456789', k=5))

class Users(Account_holder):

    def __init__(self, name, email, address, phone, account_type) -> None:
        super().__init__(name, email, address, phone, account_type)

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            Account_holder.toatl_balance+=amount
            self.transcation_history.append(f'Deposited : {amount}')

            print(f'{amount} tk has been deposited successfully to your account...Here it is ur balance : {self.balance}')

        else:
            print('Invalid amount..Please enter positive value')

    def withdraw(self,amount):
        if not self.bankrupt:
            if amount <= self.balance:
                self.balance -= amount
                Account_holder.toatl_balance -=amount
                self.transcation_history.append(f'withdrawn : {amount}')

                print(f'{amount} has been withdrawn succesfully..Here it is ur balance : {self.balance}')

            else:
                print('Sorry,You dont have enough balance')
        
        else:
            print('Bank is Bankrupt')

    def check_balance(self):
        print(f'Your balance is : {self.balance}')

    def transfer_money(self,amount,acc_no):
        if self.permission_of_transfer:
            
            if amount <= self.balance:

                who_rcv=None

                for account in Account_holder.Accounts:
                    if isinstance(account,Users)  and account.account_number == acc_no :
                        who_rcv=account
                        break

                    if who_rcv :
                        who_rcv.deposit(amount)
                        self.balance-=amount
                        Account_holder.toatl_balance-=amount
                        self.transcation_history.append(f'Transefer Amount : {amount}')

                        print(f'{amount} has been tranferred to {who_rcv.account_number}')
                        break

                    else:
                        print('This account has not been found')
                        break

            else:
                print('Insufficient balance')
        
        else:
            print('You dont have permission to transfer')
    
    
    def take_loan(self,amount):
        if self.permission_of_loan:

            if amount > 0:

                if self.number_of_loan <= 2 :
                    self.balance+=amount
                    self.amount_of_loan+=amount
                    Account_holder.toatl_balance-=amount
                    Account_holder.total_loan_amount+=amount
                    self.transcation_history.append(f'loan : {amount}')

                    print(f'You have got {amount} of tk loan from bank')

                else:
                    print('sorry,You have taken maximum number of loan already')
            
            else:
                print('please enter a valid amount')

        else:
            print('You did not fulfil the requirement of taking loan')

    def view_loan_amount(self):
        print(f'Total loan amount {self.amount_of_loan}')


    def view_transaction_history(self):
        print('\nTransaction history list')

        for history in self.transcation_history:
            print(history)



    
class Admin(Account_holder):
    
    def __init__(self, name, email, address, phone, account_type) -> None:
        super().__init__(name, email, address, phone, account_type)

    def create_an_account(self,name,email,address,phone,account_type):
        User=Users(name,email,address,phone,account_type)
        print('This account has been created successfully')

    def delete_a_user(self,acc_name):
        for acc in Account_holder.Accounts:
            if isinstance(acc,Users)  and acc.name==acc_name:
                Account_holder.Accounts.remove(acc)

                print('Deleted the account successfully')
                break

            else:
                print('There is no any account with this name')

    def see_all_user(self):
        print('Account no       Name        Email               Account type')
        for acc in Account_holder.Accounts:
            if isinstance (acc,Users):
                
                print(f'{acc.account_number}            {acc.name}      {acc.email}     {acc.account_type}')


    def total_bank_balance(self):
        print(f'Total bank balance is : {Account_holder.toatl_balance}')

    def total_loan_amount(self):
        print(f'Total loan amount : {Account_holder.total_loan_amount}')

    def loan_features(self,loan):
        if not loan:
            for acc in Account_holder.Accounts:
                if isinstance (acc,Users):
                    if loan >= 2:
                        acc.permission_of_loan = False
    
                        print('loan features is off now')
        
        else:
            for acc in Account_holder.Accounts:
                if isinstance (acc,Users):
                    if loan <= 2:
                        acc.permission_of_loan=True

                        print('loan feature is on')
    

    def bankruptt(self,dewliya):
        if dewliya:
            for acc in Account_holder.Accounts:
                if isinstance (acc,Users):
                    acc.bankrupt=True
                    print('Bankrupt!')
                    break
        
        else:
            if not dewliya:
                for acc in Account_holder.Accounts:
                    if isinstance (acc,Users):
                        acc.bankrupt=False
                        print('Not Bankrupt!')

islami=Bank('Islami Bank')
print(islami)

Rijuan=Users('Rijuan','rijuan@gmail.com','ctg',123,'savings')
Monju=Users('Monju','monju@gmail.com','Dhaka',1234,'savings')
Sifat=Users('Monju','sifat@gmail.com','Dhaka',12345,'savings')
admin=Admin('admin','admin@gmail.com','cumilla',123456,'current')


CurrentUser =None

while(True):
    if CurrentUser is None:
        print('Register or Login \n')
        op = input('Admin or User (ad/usr) :\n')

        if op== 'usr':
            opt=input('Register or Login (R/L) :\n')

            if opt=='R':
                name=input('Enter ur name\n')
                email=input('Enter ur email\n')
                address=input('Enter ur address\n')
                phone=int(input('Enter ur phone :'))
                acc_type=input('Enter ur type (sav/cur) : \n')

                Users(name,email,address,phone,acc_type)
                CurrentUser=Users(name,email,address,phone,acc_type)

            elif opt=='L':
                name=input('Enter ur name :')
                email=input('Enter ur email :')

                user=False
                for acc in Account_holder.Accounts:
                    if isinstance(acc,Users) and acc.name==name and acc.email==email :
                        CurrentUser=acc
                        user=True
                        break

                if not user:
                    print('Your information is wrong')

            else:
                print('Please select the right option')

        
        elif op=='ad':
            name=input('enter ur name : ')
            ## we can do it with password instead of using email 
            email=input('enter ur email : ')
            
            if name=='admin' and email=='admin@gmail.com':
                CurrentUser=admin

            else:
                print('Incorrect name and email')
        else:
            print('Select the right option')

    
    else:
        print('\nWelcome back')
    
        if isinstance(CurrentUser,Users):
            print('---User menu---')
            print('1.Deposit')
            print('2.Withdaw')
            print('3.Check Balance')
            print('4.Take loan')
            print('5.Total loan')
            print('6.Transfer money')
            print('7.Transaction History')
            print('8.Logout')

            op = int(input('\nChoose an option : \n'))

            if op==1:
                amountt=int(input('Enter ur amount : '))
                CurrentUser.deposit(amountt)

            elif op==2:
                amountt=int(input('Enter ur amount : '))
                CurrentUser.withdraw(amountt)

            elif op==3:
                CurrentUser.check_balance()

            elif op==4:
                amountt=int(input('Enter ur amount : '))
                CurrentUser.take_loan(amountt)

            elif op==5:
                CurrentUser.view_loan_amount()

            elif op== 6:
                amountt=int(input('Enter ur amount : '))
                acc_no=int(input('Enter reciever account number : '))
                CurrentUser.transfer_money(amountt,acc_no)

            elif op==7:
                CurrentUser.view_transaction_history()

            elif op==8:
                CurrentUser =None
                print('Logged out successfully')
            
            else:
                print('Invalid option')

        else:
            print('\n---Welcome back---\n')
            print('---Admin menu---')

            print('1.Create an account')
            print('2.Delete a user')
            print('3.See All User')
            print('4.total bank balance')
            print('5.Total loan amount')
            print('6.loan feature')
            print('7.Bankrupt')
            print('8.logout')

            op=int(input('Enter ur option : '))

            if op==1:
                name=input('Enter the name\n')
                email=input('Enter the email\n')
                address=input('Enter the address\n')
                phone=int(input('Enter the phone :'))
                acc_type=input('Enter the type (sav/cur) : \n')

                CurrentUser.create_an_account(name,email,address,phone,acc_type)

            elif op==2:
                name=input('Enter the name : ')
                sure=input('Are u sure (yes/no) :')
                if sure=='yes':
                    CurrentUser.delete_a_user(name)

            elif op==3:
                CurrentUser.see_all_user()

            elif op==4:
                CurrentUser.total_bank_balance()

            elif op==5:
                CurrentUser.total_loan_amount()

            elif op==6:
                opt=input('loan features on or off (on/off) :')
                if opt=='on':
                    CurrentUser.loan_features(True)

            elif op==7:
                sure=input('Are u bank is bankrupt?? (y/n): ')
                if sure=='y':
                    CurrentUser.bankruptt(True)
                else:
                    CurrentUser.bankruptt(False)

            elif op==8:
                CurrentUser=None
                print('logged out successfully')
                

            else:
                print('Invalid option')





    





