from Shopping import Shopping
from product import Product

def main():
    bali = Shopping("Bali Arcade")
    bali.add_user('rijuan12@gmail.com', '12', 'seller')  # Passwords as strings
    bali.add_user('monju123@gmail.com', '123', 'seller')
    bali.add_user('adhor1234@gmail.com', '1234', 'buyer')
    bali.add_user('sifat12345@gmail.com', '12345', 'buyer')
    bali.add_product(1, 'alu', 20, 5)
    bali.add_product(2, 'piyaj', 30, 10)
    bali.add_product(3, 'roshun', 100, 7)
    bali.add_product(4, 'adha', 200, 5)

    current_user = None

    while True:
        print('Please signup or signin')
        option = input('Login or register (L/R):\n').upper()
        if option == 'L':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            match = False

            for user in bali.users:
                if user['email'] == email and user['password'] == password:
                    current_user = user
                    match = True
                    print('Logging in successful')
                    break

            if not match:
                print('No users found')

            else:
                while current_user:
                    if current_user['type'] == 'seller':
                        print('---- Welcome back ----')
                        print('1. Add product')
                        print('2. Show all products')
                        print('3. Logout')

                        option = int(input("Select your option: "))
                        if option == 1:
                            product_id = int(input('Enter product ID: '))
                            name = input('Enter product name: ')
                            price = float(input('Enter product price: '))
                            quantity = int(input('Enter product quantity: '))

                            bali.add_product(product_id, name, price, quantity)

                        elif option == 2:
                            bali.show_products_list()

                        elif option == 3:
                            current_user = None
                            print('Logout successful')

                    elif current_user['type'] == 'buyer':
                        print('---- Welcome back ----')
                        print('1. Show product list')
                        print('2. Buy product')
                        print('3. Logout')

                        option = int(input("Select your option: "))
                        if option == 1:
                            bali.show_products_list()

                        elif option == 2:
                            product_id = int(input("Enter product ID: "))
                            buyer_balance = float(input("Enter your balance: "))
                            Product.buy_products(bali, product_id, buyer_balance)

                        elif option == 3:
                            current_user = None
                            print('Logout successful')

        elif option == 'R':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user_type = input("Are you a buyer or a seller? : ")
            if user_type not in ["buyer", "seller"]:
                print("Invalid user type.")
                continue
            user = bali.add_user(email, password, user_type)
            if user:
                current_user = user
                print("Registration successful!")

if __name__ == '__main__':
    main()
