N=int(input())

arr=list(map(int,input().split()))

min_num=min(arr)
max_num=max(arr)

min_index=arr.index(min_num)
max_index=arr.index(max_num)

arr[min_index],arr[max_index]=arr[max_index],arr[min_index]

print(*arr)
