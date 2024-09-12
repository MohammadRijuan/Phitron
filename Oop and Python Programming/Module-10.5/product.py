class Product:
    def __init__(self,id,name,price,quantity) -> None:
        self.product_id=id
        self.name=name
        self.price=price
        self.quantity=quantity
    
    @staticmethod
    def buy_products(self,shopping,product_id,balance_of_buyer):
        for product in shopping.product_list:
            if product['id']==int('product_id'):
                if product['quantity'] > 0 :
                    if balance_of_buyer >= product['price']:
                        product['quantity']-= 1
                        balance=balance_of_buyer = product['price']
                        print(f'here it is your left money {balance}')
                        print('u bought the product successfully')

                        return product['price']
                    else:
                        print("u dont have enough balance")
                        return 0
                else:
                    print('Stock out')
            
            else:
                product('there is no product like that')
        
        