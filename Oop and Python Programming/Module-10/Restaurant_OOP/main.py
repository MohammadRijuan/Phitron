from menu import Pizza,Burger,drinks,Menu
def main():
    menu=Menu()
    pizza1=Pizza('beef pizza',399,'large',['beef','onion'])
    menu.add_menu_item('pizza',pizza1)
    pizza2=Pizza('chicken pizza',299,'large',['chicken','onion'])
    menu.add_menu_item('pizza',pizza2)
    pizza3=Pizza('alu borta pizza',99,'large',['alu'])
    menu.add_menu_item('pizza',pizza3)


    

# call the main
if __name__ =="__main__":
    main()

