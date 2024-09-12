# lambda
# def doubled(x):
    # return x*2

doubled=lambda num : num*2
squared=lambda num: num**2
result=doubled(44)
square=squared(3)
print(result)
print(square)

add =lambda x,y : x + y
sum=add(2,5)
print(sum)

numbers=[1,3,5,7,9]
# doubled_nums=map(doubled,numbers)
doubled_nums=map(lambda x: x*2,numbers)
print(numbers)
print(list(doubled_nums))



actors=[
    {'name': 'Rijuan' ,'age': 20},
    {'name': 'nibraj' ,'age': 25},
    {'name': 'fahad' ,'age': 23},
    {'name': 'tohid' ,'age': 19},
]

juniors=filter(lambda actor : actor['age'] > 20 ,actors)
print(list(juniors))

num = lambda a:a*a
print(num(2**2))