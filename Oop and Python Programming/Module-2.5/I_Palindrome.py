
# strip ta newa jate sokol doroner space jate badh dew jai..same as 0 jehetu badh dibo tai seta mention kore dilam

N=input().strip()

reversed_N=N[::-1].strip('0')

if reversed_N==N:
    print(reversed_N)
    print("YES")

else:
    print(reversed_N)
    print("NO")