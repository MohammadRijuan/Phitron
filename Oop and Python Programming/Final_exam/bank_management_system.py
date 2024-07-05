import random

class Bank:
    Accounts=[]
    toatl_balance=[]
    loan_amount=[]

    def __init__(self,name,email,address,phone,account_type) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.phone=phone
        self.account_type=account_type
        self.account_number=[]
        self.balance=[]
        self.total_loan=[]
        self.transcation_history=[]
        self.permission_of_loan=True
        self.bankrupt=False
        self.permission_of_transfer=True
        Bank.Accounts.append(self)

    def random_account_number(self):
        return ''.join(random.choices('0123456789', k=5))


        