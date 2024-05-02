# Input A and B
A, B = map(int, input().split())

# Input the code S
S = input().strip()

# Check if the (A+1)-th character is '-' and all other characters are digits
if S[A] == '-' and S[:A].isdigit() and S[A+1:].isdigit():
    print("Yes")
else:
    print("No")
