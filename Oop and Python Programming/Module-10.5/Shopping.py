class Shopping:
    def __init__(self,name) -> None:
        self.name=name
        self.users=[]
        self.product_list=[]
    
    
    def add_user(self,email,password,user_type):
        # for user in self.users:
        #     if user['email']==email:
        #         print(f'this {email} id already exists')
        #         return
        
        user={'email':email,'password':password,'type':user_type}
        self.users.append(user)
        return user

    def add_product(self,product_id,name,price,quantity):
        product={'id':product_id,'name':name,'price':price,'quantity':quantity}
        self.product_list.append(product)

    def show_products_list(self):
        print("Showing all the Products: ")
        for products in self.products_list:
            print(
                f"Id: {products['id']}, Name: {products['name']}, Price: {products['price']}, Quantity: {products['quantity']}")
        