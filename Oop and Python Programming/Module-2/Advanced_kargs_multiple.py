# def full_name(first,second):
#     name=f'My full name is : {first} {second}'
#     return name
# # serialwise
# name=full_name('Mohammmad','Rijuan')
# print(name)


# def full_name(first,second):
#     name=f'My full name is : {first} {second}'
#     return name
# # not serial wise still will get same ans that is the power of python
# name=full_name(second='Rijuan',first='Mohammad')
# print(name)


# def **kargs
# ** 2ta dewa mane joto key ache oigulo newa
# key hcce title,addition egulo,r value hcce monju,gadha oigulo
def famous_name(first,last,**addition):
    name=f'{first} {last}'
    # print(addition['title'])
    # print(addition)

    for key,value in addition.items():
        print(key,value)
    return name
name=famous_name(first='Mohammad',last='Rijuan',title='monju',addition='gadha')
print(name)


def a_lot(x,y):
    sum=x+y
    multi=x*y
    sub=x-y
    div=x/y
    return sum,multi,sub,div

everything=a_lot(5,10)
print(everything)