# string input nilam
s=input()
# khali list nilam
listt=[]
# khali string nilam
temp=""

# protitita letter count kora hbe r ta temp e newa hbe .then jodi l r R equal hy seta list e dukano hbe ..then temp file ta kali korbo
for c in s:
    temp+=c
    if temp.count('L')==temp.count('R'):
        listt.append(temp)
        temp=""

# jotota string hbe tar length print korbo
print(len(listt))

# string tai print korbo
for i in listt:
    print(i)
