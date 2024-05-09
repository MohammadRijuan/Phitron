class Bank:

    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=100000

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

    def withdraw(self,amount):
        if amount< self.min_withdraw:
            print(f'fokir tui tk tulte parbina er kome : {self.min_withdraw}')

        elif amount > self.max_withdraw:
            print(f'bank ke fokir kore dibi..er besi tulte parbina : {self.max_withdraw}')
        
        elif amount > self.balance:
            print(f'tor teke eto tk e nai ki tulbi fokir,dek tor balance : {self.get_balance()}')


        else:
            self.balance-=amount
            print(f'here is ur withdraw amount : {amount}')
            print(f'after withdrawing ur money : {self.get_balance( )}')

islami= Bank(10000)
islami.deposit(10)
# islami.deposit(500000)
# islami.deposit(120)

print(islami.get_balance( ))

brac=Bank(2000)
# brac.withdraw(10)
# brac.withdraw(1000000)
# brac.withdraw(1050)
brac.withdraw(2005)