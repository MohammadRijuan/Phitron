from Shopping import*
from product import*
from users import *
def main():

    bali=Shopping("Bali Arcade")
    Rijuan =bali.add_user('rijuan12@gmail.com',12,'seller')
    Monju =bali.add_user('monju123@gmail.com',123,'seller')
    Adhor =bali.add_user('adhor1234@gmail.com',1234,'buyer')
    Sifat =bali.add_user('sifat12345@gmail.com',12345,'buyer')
    bali.add_product(1,'alu',20,5)
    bali.add_product(2,'piyaj',30,10)
    bali.add_product(3,'roshun',100,7)
    bali.add_product(4,'adha',200,5)

    current_user=None

    while(True):
        print('please signup or signin')
        option=input('login or register (L/R):\n')
        if option=='L':
            email=input("Enter ur email :")
            password=input("Enter ur password :")
            match=False

            for user in bali.users:
                if user['email']==email and user['password']==password:
                    current_user=user
                    match=True
                    print ('logging in successful')
                    break
            if not match:
                print('no users have found')

            else:
                if current_user['type']=='seller':
                    print('----welcome back----\n')
                    print('1.Add product')
                    print('2.Show all product')
                    print('3.logout')

                    option=int(input("Select ur option :"))
                    if option==1:
                        id=input('Enter ur product id')
                        name=input('Enter ur product name')
                        price=input('Enter ur product price')
                        quantity=input('Enter ur product quantity')

                        bali.add_product(id,name,price,quantity)

                    elif option==2:
                       bali.show_products_list()

                    elif option==3:
                       current_user=None
                       print('logout successful')

    


if __name__ == '__main__':
    main()