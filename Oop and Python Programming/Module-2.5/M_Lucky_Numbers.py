
# split dewa mane holo proti ta input k individual separate kore rakhe comma use na korleo space er agh muhurto porjnto word count kore
# apple banana likle output apple banana dibe...applebanana likle output applebanana dibe
A,B= map(int,input().split())

lucky_number=[]

# A teke suru B te ses
for num in range(A,B+1):
    if all(digit in ['4','7'] for digit in str(num)):
        lucky_number.append(num)

if lucky_number:
    # * na dile bracket akare ans dibe
    print(*lucky_number)
else:
    print(-1)


# by using array we can solve it as well

arr = [int(x) for x in input().split()]

A,B=arr[0],arr[1]

lucky_number=[]

for num in range(A,B+1):
    if all(digit in ['4','7'] for digit in str(num)):
        lucky_number.append(num)

if lucky_number:
    print(*lucky_number)

else:
    print(-1)

