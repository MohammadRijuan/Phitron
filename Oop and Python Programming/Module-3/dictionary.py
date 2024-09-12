# key value pair
# dictionary
# object
# hash table
# overlap with set

persons={'name' : 'Rijuan','address':'bahaddarhat', 'age':20}
print(persons.keys())
print(persons.values())
print(persons['age'])
persons['course']='phitron'
persons['name']='rijuan monju'
print(persons)


for item in persons:
    print(item)

# special dictionary looping where we will get along wid value
for key,value in persons.items():
    print(key,value)


numbers=[10,20,30,40,50]
# enumerate will help u to give ur output along wid index
for i,num in enumerate(numbers):
    print(i,num)
# we will get everything from dictionary method of python