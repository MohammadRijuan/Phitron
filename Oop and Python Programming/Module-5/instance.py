class shop:

    # eikane initialize e cart declare korle buyer onusare separate cart dekabe...instant dibe
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]


    def add_to_cart(self,item):
        self.cart.append(item)

myShop=shop('Rijuan')

myShop.add_to_cart('car')
myShop.add_to_cart('macbook')

print(myShop.buyer,myShop.cart)

apu=shop('apu')

apu.add_to_cart('ring')
apu.add_to_cart('faltu jinish')
print(apu.buyer,apu.cart)