numbers=[1,2,3,4,5]
# push
numbers.append(8)
print(numbers)

# joto index bolbo toto te insert korbe
numbers.insert(0,10)
print(numbers)

numbers.remove(4)
print(numbers)

# last item remove korbe
numbers.pop()
print(numbers)

# index searching
index=numbers.index(2)
print(index)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)