# tuple holo first bracket e elememnt dewa...r list 2nd bracket e dewa hy
def multiple():
    return 3,4
# print(multiple())

things=['mobile','phone','charger']
thing='fan','mug','watch'
print(type(things))
print(type(thing))

if 'phone' in things:
    print('exist')
print(thing[0])
print(things[0])

for item in thing:
    print(item)

print(len(things))

mega=([2,3,4],[1,4,5])
print(type(mega))
print(mega)

print(mega[0])
# if i want to change any index element
mega[0][2]=546
print(mega)