# static attribute (class method)
# static method @staticmethod
# class method @classmethod
# differences between class method and static method

class shopping:
    cart=[]
    origin='china'

    def __init__(self,name,location) -> None:
        # instance_attribute
        self.name='Bali Arcade' 
        self.location='Chawkbazar'

    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'buying : {item} for price  : {price} tk remaining :{remaining}')

    def hudhai_deki(self):
        print('janina ki kortesi')

    @staticmethod
    def add(a,b):
        result= a + b
        print(result)

    @classmethod
    def mul(self,a,b):
        result= a*b
        print(result)

Bali=shopping("Bali","Bahaddarhat")
Bali.purchase('dim',10,100)

# eikhane instance use kore cls call kore 'a' ta print koreni...karon self e ki dibe...ata tho desire attribute na
shopping.purchase('a','dim',12,120)
# terminal e missing 1 argument show korbe
# shopping.hudhai_deki()

# but ata te clearly output dibe
Bali.hudhai_deki()

# ekon direct class e function use kore @classmethod declare korle tiktak output dibe
shopping.mul(6,4)
shopping.add(6,4)

        