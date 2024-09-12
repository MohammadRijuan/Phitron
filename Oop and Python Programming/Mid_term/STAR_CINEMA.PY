class Star_cinema:
    hall_list=[]
     
    @classmethod
    def entry_hall(self,token):
        self.hall_list.append(token)

class hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self._seats={}
        self.__show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        

    def entry_show(self,id,movie_name,time):
        show=(id,movie_name,time)
        self.__show_list.append(show)

        self._seats[id]=[]

        for i in range(self.rows):
            col=[]
            for j in range(self.cols):
                col.append(0)
            self._seats[id].append(col)

    def book_seats(self,id,row,col):
        movie_id=False

        for i in self.__show_list:
            if movie_id==id:
                movie_id=True
                break

        if movie_id !=id:
            print('You have enterted wrong movie id...There is no any movie along with this id')

        show_seats=self._seats.get(id)

        if show_seats[row][col]==1:
            print(f' seat of row:{row} and col:{col} are booked')
        
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            print(f'You information is wrong! please check your row/col again! ')

        else:
            show_seats[row][col]=1
            print('You have booked a seat successfully')


    def view_show_list(self):
        print("\nAvailable Movies:\n")
        print(f'     Movie Id  \t Moive Name \t Time  ')
        
        for show in self.__show_list:
            print(f'\t{show[0]}   \t  {show[1]}\t{show[2]}')

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


Hall = hall(rows=5, cols=5, hall_no=1)

Hall.entry_show(11, "pathan", "10:00")
Hall.entry_show(13, "jawan", "\t1:00")
Hall.entry_show(12, "tiger", "\t2:00")

Star_cinema.entry_hall(Hall)

while True:

    print("\nWelcome to our theatre\n")
    print("1. View Movie Name")
    print("2. View Available Seats")
    print("3. Book Seats")
    print("4. Exit")

    option = int(input("Enter Option :"))

    if (option == 1):
        Hall.view_show_list()

    elif option == 2:
        id = int(input("what do you wanna see ?Enter movie id please: "))
        Hall.view_available_seats(id)

    elif option == 3:
        id = int(input("Enter your movie id : "))
        ticket = int(input("How many tickets do you want to buy? :"))

        for _ in range(ticket):
            row = int(input("Enter the number of row : "))
            col = int(input("Enter the number of col : "))
            row -= 1
            col -= 1
            Hall.book_seats(id, row, col)

    elif option == 4:
        print("Ok Bye..Take care Yourself")
        break

    else:
        print("Please check your input again and select the right option! ")




        
        

    