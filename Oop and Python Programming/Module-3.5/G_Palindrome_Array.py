N=input()

arr=list(map(int,input().split()))
# arr=[int(i) for i in input().split(" ")]

reversed_arr=arr[::-1]

if arr==reversed_arr:
    print("YES")
else:
    print("NO")