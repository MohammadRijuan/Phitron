# global variable
balance=300000

def buy(items,price):
    # if i have to access the value of global value then we have to use (global) in the function ..otherwise we cannot access the value
    # we can use local variable but cannot access the global
    global balance
    print(f'previous balance',balance)
    balance=balance-price
    print(f'after buying {items}',balance)

buy('iphone',142000)
print('global balance after buy',balance)