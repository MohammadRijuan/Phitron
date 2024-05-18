class book:
    def __init__(self,id,name,quant) -> None:
        self.id=id
        self.name=name
        self.quantity=quant

class user:
    def __init__(self,id,name,password) -> None:
        self.id=id
        self.name=name
        self.password=password
        self.borrowed_books=[]
        self.returned_books=[]

class library:
    def __init__(self,name) -> None:
        self.name=name
        self.users=[]
        self.books=[]

    def addBook(self,id,name,quant):
        Book=book(id,name,quant)
        self.books.append(Book)
        print(f'{Book.name} added successfully')

    def adduser(self,id,name,password):
        User=user(id,name,password)
        self.users.append(User)
        return User
    
    def borrowbooks(self,user,token):

        for book in self.books:
            if book.name==token:
                if book in user.borrowed_books:
                    print('Already borrowed\n')
                    return
                elif book.quantity==0:
                    print('No copy available\n')
                    return
                
                else:
                    user.borrowed_books.append(book)
                    book.quantity-=1
                    print('borrowed books successfully')
                    return
        print(f'not found any book with name{token}')


    def returnbooks(self,user,token):

        for book in self.books:
            if book.name==token:
                if book in user.borrowed_books:
                    book.quantity+=1
                    user.returned_books.append(book)
                    user.borrowed_books.remove(book)
                elif book.quantity==0:
                    print('No copy available\n')
                    return
                
        print(f'not found any book with name{token}')
                    


batighor=library("Batighor")
admin=batighor.adduser(100,"admin",1000)
Rijuan=batighor.adduser(101,"Rijuan",1001)
Monju=batighor.adduser(102,"Monju",1002)

current_user=None

while(True):
    if current_user==None:
        print("No one logged in\n")

        option=input("Login or Register (L/R) : ")

        if option=='L':
            id=int(input("Enter ur id : "))
            password=int(input("Enter ur password : "))

            match=False

            for users in batighor.users:
                if users.id==id and users.password==password:
                    current_user=users
                    match=True
                    break
            if match==False:
                print('No user have found\n')
                break

        
        elif option=="R":
            id=int(input("Enter ur id :\n"))
            name=input("Enter ur name :\n")
            password=int(input("Enter ur password :\n"))

            for users in batighor.users:
                if users.id==id:
                    print("users already exist")

            users=batighor.adduser(id,name,password)
            current_user=users
    
    else:
        print(f"welcome back {current_user.name}\n")

        if current_user.name=="admin":

            print("options :\n")
            print("1.Add book ")
            print("2.Add user ")
            print("3.Show all books ")
            print("4.Logout ")

            ch=int(input("Enter option :\n"))

            if ch==1:
                id=int(input("Book id please :\n"))
                name=input("Book name please :\n")
                quan=int(input("how many do u wanna added :\n"))

                batighor.addBook(id,name,quan)

            elif ch == 3:
                print("ID\tName\tQuantity")
                for Book in batighor.books:  # Loop through each book object in the list
                    print(f"{Book.id}\t{Book.name}\t{Book.quantity}")
                print('\n')


            elif ch==4:
                current_user=None

        else:
            print("options :\n")
            print("1.Borrow books ")
            print("2.Show borrowed books ")
            print("3.Show all books ")
            print("4.Show history ")
            print("5.Logout ")

            ch=int(input("Enter option :\n"))

            if ch==1:
                batighor.name=input('Enter book name :')
                batighor.borrowbooks(current_user,name)

            elif ch==2:
                batighor.name=input('Enter book name :')
                batighor.returnbooks(current_user,name)

            elif ch == 3:
                print("\nborrowed books :\n")
                for Book in current_user.borrowed_books:  # Loop through each book object in the list
                    print(f"{Book.id}\t{Book.name}\t{Book.quantity}")
                print('\n')

            elif ch == 4:
                print("\nHistory\n")
                for Book in current_user.returned_books:  # Loop through each book object in the list
                    print(f"{Book.id}\t{Book.name}\t{Book.quantity}")
                print('\n')

            elif ch==5:
                current_user==None


        