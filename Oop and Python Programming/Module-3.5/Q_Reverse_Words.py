string=input().split()

for i , word in enumerate(string):
    if(i==len(string)-1 ):
        print(word[::-1],end="")
    else:
        print(word[::-1],end=" ")



# another way to solve it

# Take input
S = input()

# Split the string into words
words = S.split()

# Reverse each word and join them back together with spaces
reversed_words = [word[::-1] for word in words]
reversed_S = ' '.join(reversed_words)

# Print the result
print(reversed_S)
