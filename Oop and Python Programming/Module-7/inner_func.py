# 1
def double_decker():
    print('ami valo aci')

    def fun():
        print('kub moja lagce')
        return 'ata none er bodle seta bujar jnno'
    
    return fun

# print(double_decker())
print(double_decker()())

# 2
def hello(work):
    print('mon aj ura ura')
    # print(work)

    # ei process coding function tar jonno soho
    work()
    print('uff ki joss programming')

# hello('juice')

def coding():
    print('amar aj ato valo lagce coding kortwe')

hello(coding)

def slepp():
    print('sey gum hbe')

hello(slepp)