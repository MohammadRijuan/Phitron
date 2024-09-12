# base class , parent class

class vehicle:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price

    def __repr__(self) -> str:
        return f'name : {self.name} , price : {self.price}'


class truck(vehicle):
    def __init__(self, name, price,weight) -> None:
        self.weight=weight
        super().__init__(name, price)

class Bus(vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat=seat
        super().__init__(name, price)        

class pick_up_truck(truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperature=temperature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        return f'Ac Bus : {self.name} ,price : {self.price} ,available seat : {self.seat} ,temperature will be : {self.temperature}'

Marsa=ACBus("Marsa",21000000,35,"22 degree")
print(Marsa)



cnt = {}
i = 1
if i not in cnt:
    cnt[i] = 1
else:
    cnt[i] += 1

print(cnt)