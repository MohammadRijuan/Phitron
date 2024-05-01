# taking input
N=int(input()) 

numbers=list(map(int,input().split()))

# finding max and min
max_num=max(numbers)
min_num=min(numbers)

# serial of index
max_index=numbers.index(max_num)
min_index=numbers.index(min_num)

# swap process
numbers[min_index],numbers[max_index]=numbers[max_index],numbers[min_index]

print(*numbers)