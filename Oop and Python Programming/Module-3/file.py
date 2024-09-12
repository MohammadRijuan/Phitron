# .csv comma seperate value
# .txt text file

# it will help u to open a file automatically
# w dile write korbe
with open('message.txt','w') as file:
    file.write('Rijuan will be boss soon')

# a dile append means add korbe
with open('message.txt','a') as file:
    file.write('Rijuan will be boss soon')

# r dile read korbe
with open('message.txt','r') as file:
    text=file.read()
    print(text)