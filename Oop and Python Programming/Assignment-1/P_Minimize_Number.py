n=input()

arr=[int(i) for i in input().split()]

flag=True
cnt=0

while flag is True:
    for i,num in enumerate(arr):
        if num%2 == 1:
            flag=False
            break
        else:
            arr[i]/=2

    if flag is True: 
        cnt+=1

print(cnt)
