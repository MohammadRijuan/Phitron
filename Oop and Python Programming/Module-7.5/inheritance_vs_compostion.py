# inheritance
class junkFood:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price


    def taste(self):
        print('its so yummy')

class burger(junkFood):
    def __init__(self, name, price) -> None:
        super().__init__(name, price)

    def taste(self):
        print('too much yummy')

class hotdog(junkFood):
    def __init__(self, name, price) -> None:
        super().__init__(name, price)

    
    def taste(self):
        pass

hottdog=hotdog('hotdog',120)
hottdog.taste()

burger_king=burger('cheese burger',250)
burger_king.taste()
        