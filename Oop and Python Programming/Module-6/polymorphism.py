class Animal:
    def __init__(self,name) -> None:
        self.name=name

    def make_sound(self):
        print('goru dake hamba hamba')

class cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('meaow meaow')

class crow(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('ka ka')

class dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    # if i dont print any sound ofn dog then it will provide the sound of animal what i have given
    # like animal cls e goru dake hamba hamba...oita dog er class e output dibe karon ami dog er kono sound di ni
    def make_sound(self):
        return super().make_sound()
    
jangli_billi=cat('jangli billi')
jangli_billi.make_sound()

hawwo=crow('hawwo')
hawwo.make_sound()

kukur=dog('kukur')
kukur.make_sound()
        