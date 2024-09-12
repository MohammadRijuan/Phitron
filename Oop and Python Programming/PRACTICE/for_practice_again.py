class jalsha_cinema:
    hall_list=[]

    @classmethod
    def entry_hall(self,token):
        self.hall_list.append(token)

class hall:
    def __init__(self,cols,rows,hall_no) -> None:
        self._seats={}
        self.__show_list=[]
        self.cols=cols
        self.rows=rows
        self.hall_no=hall_no

    def entry_show(self,id,movie_name,time):
        show=(id,movie_name,time)
        self.__show_list.append(show)

        self._seats[id]=[]

        for i in range (self.rows):
            row=[]
            for j in range (self.cols):
                row.append(0)
            self._seats[id].append(row)

    def books_seats(self,id,row,col):
        valid_movie=False
        
        for i in self.__show_list:

            if valid_movie==id:
                valid_movie=True
                break
        
        if valid_movie !=id:
            print('u have placed a wrong movie id')

        show_seats=self._seats.get(id)

        if show_seats[row][col]==1:
            print('sorry this seats has been booked')

        if not (0<=row < self.rows and 0<=col < self.cols):
            print('please check ur row/col again')

        else:
            show_seats[row][col]=1
            print('u have successfully booked a seat')

    def view_show_list(self):
        print('\navailable movies\n')
        print('Id\t Movie name \t time\t')

        for show in self.__show_list:
            print(f'{show[0]} \t {show[1]} \t \t  {show[2]}')

    def view_available_seats(self,id):
        if id not in self._seats:
            print("invalid movie id")
            return
        print(f'available seats for this movie id: {id}')

        for col in self._seats[id]:
            print("{ ", end="")
            for seat in col:
                if seat == 0:
                    print("0", end=" ")
                else:
                    print("1", end=" ")
            print("}")


Hall=hall(cols=5,rows=5,hall_no=1)
Hall.entry_show(101,"war",'\t10.00')
Hall.entry_show(102,"tarzan",12.00)
Hall.entry_show(103,"captain america",2.00)

jalsha_cinema.entry_hall(Hall)


while(True):
    print("\nWelcome to Jalsha Cinema\n")
    print("1. View Movie name")
    print("2. View available seats")
    print("3. Booking seats")
    print("4. Exit")

    option=int(input("Enter ur options: "))

    if option==1:
        Hall.view_show_list()

    elif option==2:
        id = int(input("what do you wanna see ?Enter movie id please: "))
        Hall.view_available_seats(id)

    elif option==3:
        id=int(input('movie id :'))
        ticket=int(input('How many tickets do want to buy?'))

        for _ in range(ticket):
            row=int(input('Enter ur row:'))
            col=int(input('Enter ur col:'))
            row-=1
            col-=1
            Hall.books_seats(id,row,col)

    elif option==4:
        print('bye bye')

    else:
        print('please enter the  right option')










        