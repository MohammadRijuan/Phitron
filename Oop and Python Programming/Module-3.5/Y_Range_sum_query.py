N, Q = map(int, input().split())
Arr = list(map(int, input().split()))


def sum_query(L, R):
    return sum(Arr[L-1:R])


for _ in range(Q):
    L, R = map(int, input().split())
    print(sum_query(L, R))
