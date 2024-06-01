from User import*
class Bank:
    def __init__(self,name,branch,initial_amount) -> None:
        self.name=name
        self.branch=branch
        self.balance=initial_amount
        self.users=[]
        self.admins=[]
        self.loan=True
        self.amount_of_loan=0
        self.bankrupt=False

    def __repr__(self) -> str:
        return f'>>>>>> {self.name} <<<<<<'
    
    def total_balance(self):
        print(f'{self.balance}')

    