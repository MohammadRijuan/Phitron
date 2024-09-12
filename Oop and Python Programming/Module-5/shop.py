class Shop:

    cart=[]

    def __init__(self,buyer):
        self.buyer=buyer

    def Add_to_cart(self,item):
        self.cart.append(item)


myShop=Shop('Rijuan')
myShop.Add_to_cart('Audi car')
myShop.Add_to_cart('Macbook')

print(myShop.buyer,myShop.cart)

apu=Shop('Apu')
apu.Add_to_cart('ring')
apu.Add_to_cart('cap')
print(apu.buyer,apu.cart)

# ei method e onner cart gulor sthe mixed hoye jai