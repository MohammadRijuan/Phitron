def call():
    print('calling someone i donno')
    return "call done"
# call function jodi class e reke self variable dile class er call keo cl kora jvbe
class Phone:
    Brand='Samsung'
    price=5000
    Features=['call','facebooking','whatsapp']
    

    # class er vitorer function gulo te obossoy self dite hbe
    def call(self):
       print('call one person')

    def send_sms(self,phone,sms):
        text=f'sending sms to :{ phone} and message : {sms}'
        return text

my_phone=Phone()
# print(my_phone)
print(my_phone.Features)
my_phone.call()
# eibve function ke call korle none output dibe..uporer moto call korte hbe
print( my_phone.call( ))

result=my_phone.send_sms(1833992529,'i miss u')
print(result )