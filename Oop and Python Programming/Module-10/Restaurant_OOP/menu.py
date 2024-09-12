class Food:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
        self.cooking_time=15

class Burger(Food):
    def __init__(self, name, price,meat,ingredients) -> None:
        super().__init__(name, price)
        self.meat=meat
        self.ingrediants=ingredients

class Pizza(Food):
    def __init__(self, name, price,size,topings) -> None:
        super().__init__(name, price)
        self.size=size
        self.topings=topings

class drinks(Food):
    def __init__(self, name, price,isCold=True) -> None:
        super().__init__(name, price)
        self.isCold=isCold

# composition- onk item thakbe
class Menu:
    def __init__(self) -> None:
        self.pizzas=[]
        self.bugers=[]
        self.drinks=[]

    def add_menu_item(self,item_type,item):
        if item_type=='pizza':
            self.pizzas.append(item)

        elif item_type=='burger':
            self.bugers.append(item)

        elif item_type=='drink':
            self.drinks.append(item) 

    def remove_pizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)

    def remove_burger(self,burger):
        if burger in self.bugers:
            self.bugers.remove(burger)

    def remove_drinks(self,drink):
        if drink in self.drinks:
            self.drinks.remove(drink)

    def show_menu(self):
        for pizza in self.pizzas:
            print(f'name: {pizza.name} , price is-> {pizza.price}')

        for burgers in self.bugers:
            print(f'name: {burgers.name} , price is-> {burgers.price}')

        for drinks in self.drinks:
            print(f'name: {drinks.name} , price is-> {drinks.price}')

        

        