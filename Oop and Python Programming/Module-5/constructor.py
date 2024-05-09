class Phone:
    manufacture='Bangladesh'

    # initialize as a constructor
    def __init__(self, name, brand, price):
        self.name=name
        self.brand=brand
        self.price=price

    def send_sms(self, Phone,sms):
        text=f'sending text to : {Phone} {sms}'
        print(text)

my_phone=Phone('Abbu','Redmi',10000)
print(my_phone.name,my_phone.brand,my_phone.price)

my_phone.send_sms(1833992529,'Gadha')

sis_phone=Phone('Apu','Redmi',12000)
print(sis_phone.name,sis_phone.brand,sis_phone.price)

