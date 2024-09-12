class shop:
    def __init__(self) -> None:
        self.products=[]

    def add_product(self,item):
        self.item=item
        
        self.products.append(item)

    def buy_product(self, name):
        for product in self.products:
            if product.name == name:
                return f'This product is available: {product.name}'
        return 'This product is not available'

class product:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price

startech = shop()
p1 = product('Phone', 70000)
p2 = product('Laptop', 120000)
p3 = product('Monitor', 27000)
p4 = product('Casing', 12000)

startech.add_product(p1)
startech.add_product(p2)
startech.add_product(p3)
startech.add_product(p4)

print(startech.buy_product('Monitor'))
print(startech.buy_product('Processor'))
        