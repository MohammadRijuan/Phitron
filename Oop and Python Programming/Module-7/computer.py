# inheritance vs composition

class cpu:
    def __init__(self,cores) -> None:
        self.cores=cores

class ram:
    def __init__(self,size) -> None:
        self.size=size

class hdd:
    def __init__(self,fan) -> None:
        self.fan=fan

# computer 'has a' cpu
# computer 'has a' ram
# computer 'has a' hdd
class computer:
    def __init__(self,cores,size,fan) -> None:
        self.cpu=cpu(cores)
        self.ram=ram(size)
        self.hdd=hdd(fan)

    
        
hp=computer(8,12,'big')

        