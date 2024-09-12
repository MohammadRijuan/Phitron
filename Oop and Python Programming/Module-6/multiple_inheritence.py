class family:
    def __init__(self,address) -> None:
        self.address=address

class school:
    def __init__(self,level,id) -> None:
        self.level=level
        self.id=id

class sports:
    def __init__(self,game) -> None:
        self.game=game

class students(family,school,sports):
    def __init__(self,name, address,level,id,game) -> None:
        self.name=name
        family.__init__(self,address)
        school.__init__(self,level,id)
        sports.__init__(self,game)

    def __repr__(self) -> str:
        return f'I am {self.name}..I am from {self.address}..I studied at {self.level}..My id no is {self.id}..I love to play {self.game}'
    
myself=students('Rijuan',"CTG",14,4,"cricket")
print(myself)
        
        