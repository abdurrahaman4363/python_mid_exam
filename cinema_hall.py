# 1 number 
class Star_Cinema:
    hall_list  = []

    def __init__(self) -> None:
        pass

    def entry_hall(self,obj):
        self.hall_list.append(obj)

# 2 number
class Hall(Star_Cinema):

    def __init__(self,rows,cols,hall_no):

        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        super().__init__()
        self.entry_hall(self)

    # 3 number
    def entry_show(self,id,movie_name,time):


        info = (id, movie_name, time)
        self.__show_list.append(info)

        seatList = [
            [0 for _ in range(self.__cols)] for _ in range(self.__rows)
        ]  
        self.__seats[id] = seatList


    # 4 number
    def book_seats(self,id,seats_tuple):
        if id in self.__seats:
            seats = self.__seats[id]
            for row, col in seats_tuple:
                seats = self.__seats[id]
                if 0 <= row < self.__rows and 0 <= col < self.__cols:
                    if seats[row][col] == 0:
                        seats[row][col] = 1
                        print(f"Seat ({row}, {col}) booked successfully for {id}.") # 8 number
                    else:
                        print(f"Seat ({row}, {col}) is already booked for {id}.") # 8 number
                else:
                    print(f"Seat ({row}, {col}) is not available for {id}.") # 8 number
        else:
            print(f"OPPPPPs ID {show_id} IS NOT FOUND.") # 8 number


    # 5 number
    def view_show_list(self):
            for id, movie_name, time in self.__show_list:
                print(f"ID: {id}, Movie: {movie_name}, Time: {time}")  
                
    # 6 number                     
    def view_available_seats(self, id):
        if id in self.__seats:
            print(f"AVAILABLE SEATS FOR SHOW {id}:")

            seats = self.__seats[id]

            for i in range(self.__rows):
                for j in range(self.__cols):
                    if seats[i][j] == 0:
                        print(f"SEAT: {i}, {j}")

            print("\nUpdate Seats matrix:")
            for row in range(self.__rows):
                for col in range(self.__cols):
                    if seats[row][col] == 0:
                        print('0', end=" ")  
                    else:
                        print('1', end=" ")  
                print() 
        else:
           print(f"OPPPPPs ID {show_id} IS NOT FOUND.") # 8 number
                  




hall_book = Hall(5, 7, 100)
hall_book.entry_show(id="100", movie_name="TOM", time="06/10/2002  6.00PM")
hall_book.entry_show(id="300", movie_name="ACTION", time="07/1/2023  1.00PM")
hall_book.entry_show(id="500", movie_name="COMMEDY", time="12/6/2023  10.00PM")

# 7 number
while True:
    print("OPTION: ")
    print('--------------------------------------')
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    print('-------------------------------------')
    
    option = int(input("ENTER OPTION : "))
    
    if option == 1:
        hall_book.view_show_list()
    
    elif option == 2:
        show_id = input("ENTER SHOW ID: ")
        hall_book.view_available_seats(show_id)
    
    elif option == 3:
        show_id = input("ENTER SHOW ID: ")
        number_of_ticket = int(input("Number of Tickets: "))
        seats_book = [
            (int(input("ENTER SEAT ROW: ")), int(input("ENTER SEAT COLUMN: ")))
            for _ in range(number_of_ticket)
        ]
        hall_book.book_seats(id=show_id, seats_tuple=seats_book)

    elif option == 4:
        break
    else:
        print("Invalid option.")
        break