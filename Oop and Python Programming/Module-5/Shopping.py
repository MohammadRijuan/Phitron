class Shopping:
    shopping_name='Bali arcade'

    def __init__(self,name):
        self.name=name
        self.cart=[]

    def Add_to_cart(self,item,price,quantity):
        product={'item' : item , 'price' : price , 'quantity' : quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total=0

        for item in self.cart:
            # print(item)
            total+= item['price'] * item['quantity']
        print('total price',total)
        if amount<total:
            print(f'please provide money {total-amount} more')
        else:
            extra=amount-total
            print(f'here is ur {item} and extra money :{extra}')

Customer=Shopping('Rijuan')
Customer.Add_to_cart('alu',50,5)
Customer.Add_to_cart('piyaj',10,6)
Customer.Add_to_cart('lobon',30,2)

print(Customer.cart)
Customer.checkout(500)