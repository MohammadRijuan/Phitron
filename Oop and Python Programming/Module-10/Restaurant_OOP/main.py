from menu import Pizza,Burger,drinks,Menu
from restaurant import Restaurant
from users import chef,Customer,server,Manager
from order import order

def main():
    menu=Menu()

    # pizza
    pizza1=Pizza('beef pizza',399,'large',['beef','onion'])
    menu.add_menu_item('pizza',pizza1)
    pizza2=Pizza('chicken pizza',299,'large',['chicken','onion'])
    menu.add_menu_item('pizza',pizza2)
    pizza3=Pizza('alu borta pizza',99,'large',['alu'])
    menu.add_menu_item('pizza',pizza3)

    # burger
    burger1=Burger('cheese burger',150,'beef','cheese')
    menu.add_menu_item('burger',burger1)
    burger2=Burger('chicken burger',120,'chicken','letuce')
    menu.add_menu_item('burger',burger2)
    burger3=Burger('egg burger',60,'egg','cucumber')
    menu.add_menu_item('burger',burger3)

    # drink
    coke=drinks('coke',30,True)
    menu.add_menu_item('drink',coke)
    coffe=drinks('coffe',20,False)
    menu.add_menu_item('drink',coffe)

    # show menu
    menu.show_menu()

    kacchi_dine=Restaurant('kacchi dine',200,menu)
    
    # add employees
    manager=Manager('Rijuan',1833992529,'abcgmail.com','Bahaddarhat',20000,'1st jan','core')
    kacchi_dine.add_employee('manager',manager)

    Chef=chef('Rustom baburchi',123,'xyazgmail.com','Dhaka',30000,'1st jan','chef','bireni')
    kacchi_dine.add_employee('chef',Chef)

    Server=server('Abul',123,'xyabzgmail.com','sylhet',12000,'1st jan','server')
    kacchi_dine.add_employee('server',Server)
    
    # show employess
    kacchi_dine.show_employees()

    # customer 1
    Customer1=Customer('sakib khan',12345,'qwegmail.com','dhaka',5000,'pizza')
    order1=order(Customer1,[pizza1,coffe])

    Customer1.pay_for_order(order1)

    kacchi_dine.add_order(order1)

    # customer1 paying for order1
    kacchi_dine.recieve_amount(order1,2000,Customer1)

    print('revenue and balance after first customer',kacchi_dine.revenue,kacchi_dine.balance)

    # customer 2
    Customer2=Customer('Arbaz khan',1234567,'qwegmail.com','india',5000,'pizza')
    order2=order(Customer2,[pizza1,burger1,coffe])

    Customer2.pay_for_order(order2)

    kacchi_dine.add_order(order2)

    # customer1 paying for order1
    kacchi_dine.recieve_amount(order2,3000,Customer2)
    
    
    print('revenue and balance after second customer',kacchi_dine.revenue,kacchi_dine.balance)


    # pay rent
    kacchi_dine.pay_expense(kacchi_dine.rent,'rent')
    print('after rent',kacchi_dine.revenue,kacchi_dine.balance,kacchi_dine.expense)

    # salary
    kacchi_dine.pay_salary(Chef)
    print('after salary',kacchi_dine.revenue,kacchi_dine.balance,kacchi_dine.expense)



    

# call the main
if __name__ =="__main__":
    main()

