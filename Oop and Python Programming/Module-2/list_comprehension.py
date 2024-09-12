numbers=[1,2,3,4,7,8,6]
odds=[]

for num in numbers:
    if num%2==1:
        odds.append(num)
print(odds)

# shortcut in 1 line...readable na
odd_nums=[num for num in numbers if num%2==1]
print(odd_nums)

players=['sakib','Rijuan']
ages=[10,20]

for player in players:
    print('player: ',player)
    for age in ages:
        print(player,age)

