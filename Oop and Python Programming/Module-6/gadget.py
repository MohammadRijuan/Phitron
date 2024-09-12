class laptop:
    def __init__(self,brand,color,price,memory) -> None:
        self.brand=brand
        self.color=color
        self.price=price
        self.memory=memory

    def run(self):
        return f'Running laptop {self.brand}'
    
    def coding(self):
        return f'practicing python at {self.brand}'
    
class Phone:
    def __init__(self,brand,color,price,sim,number) -> None:
        self.brand=brand
        self.color=color
        self.price=price
        self.sim=sim
        self.number=number

    def run(self):
        return f'running mobile {self.brand}'
    
    def sending_sms(self):
        return f'sending sms to : {self.number}'

class Cameras:
    def __init__(self,brand,color,price,lens) -> None:
        self.brand=brand
        self.color=color
        self.price=price
        self.lens=lens

    def run(self):
        return f'running smoothly {self.brand}'
    
    def lens(self):
        return f'Changed successful'
    


