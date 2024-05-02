
def smallest_number(N,arr):
    min_sum=float('Inf')

    for i in range(N):
        for j in range(i+1,N):
            curr_sum=arr[i]+arr[j]+j-i
            min_sum=min(min_sum,curr_sum)
    return min_sum

T=int(input())

for _ in range(T):

    N=int(input())

    arr=list(map(int,input().split()))

print(smallest_number(N,arr))