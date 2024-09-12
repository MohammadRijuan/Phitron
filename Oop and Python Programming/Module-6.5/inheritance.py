class product:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price

class shop:
    def __init__(self) -> None:
        self.list=[]

    def add_product(self,item):
        self.list.append(item)

class discounts(product):
    def __init__(self, name, price,discount) -> None:
        self.discount=discount
        super().__init__(name, price)

    def get_discounted_price(self):
        return self.price * (1 - self.discount)
    
text = shop()
text1 = product("lychee", 100)
text2 = product("mango", 120)
text.add_product(text1)
text.add_product(text2)

product_ans = discounts("onion", 700, 0.2)  # Discounted price with 10% discount
text.add_product(product_ans)

for item in text.list:
    if isinstance(item, discounts):
        print(f'Name: {item.name}, Price: ${item.price}, Discount: {item.discount}, Discounted Price: ${item.get_discounted_price()}')
    else:
        print(f'Name: {item.name}, Price: ${item.price}')

        