class shopping:
    cart=[]
    origin ='BAngladesh'

    def __init__(self,name,location) -> None:
        self.name='sky park'
        self.location='Bahaddarhat'

    def purchase(self,goods,price,amount):
        remaining=amount-price
        print(f'buying {goods} for {price}tk..remaining : {remaining}')

    def dekbo_sudu(self):
        print('kinbo na kicu')

    @classmethod
    # i have used class method then it will require self in the function but when i will call the function there will no need any object instead of self position
    def kinbo_eibar(self,item):
        print(f'yeah,i have bought {item}')

    @staticmethod
    # in static method there will no need any self on the class
    def sob_kinbo(item,price,quantity):
        total=quantity*price
        print(f'i m buying {item} for {price}tk..total will be: {total}')

moti=shopping('moti tower','chawkbazar')

moti.purchase('dim',80,100)

# here a is not provide as a output but it still required a value in its position
shopping.purchase('a','dim',70,100)

# if i didnot put anything on its self postion then it will give an error
# shopping.purchase('dim',70,100)

shopping.kinbo_eibar('dim')
shopping.sob_kinbo('pen',5,10)
        