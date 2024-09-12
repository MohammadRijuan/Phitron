#encapsultion mean -> hide details
#access modifier : public, protected, private

class Bank:
    def __init__(self,holder_name,branch,initial_deposit) -> None:
        self.holder_name=holder_name #public
        self._branch='chawkbazar'  # 1ta underscore _ dewa mane holo protected
        self.__balance=initial_deposit #2ta __ underscore dewa mane holo private

    def deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance-=amount
            return amount
        else:
            return f'You dont have enough fund'

# access public attribute
Rijuan=Bank("Rijuan","Bahaddarhat",100000)
# Rijuan.balance=0
Rijuan.holder_name="Sifat"
print(Rijuan.holder_name)

# Accessing private attribute indirectly using a method
Rijuan.deposit(50000)
print(Rijuan.get_balance())

# Attempting to access protected attribute directly
print(Rijuan._branch)

# Attempting to access private attribute directly (not recommended)
print(Rijuan._Bank__balance)  # Uncommenting this will print 150000

# withdrawing_money
Rijuan.withdraw(5000)
print(Rijuan.get_balance())
        