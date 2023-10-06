class Star_Cinema:
    __hall_list=[]
    @classmethod
    def entry_hall(cls, hall_obj):
        if isinstance(hall_obj, Hall):
            cls.__hall_list.append(hall_obj)
            print(f"Hall {hall_obj._hall_no} added to the hall_list.")
        else:
            print("Invalid input. Please provide a Hall object.")
    @classmethod
    def get_hall_list(cls):
        return cls.__hall_list


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__show_list = [] 
        self.__rows = rows 
        self.__cols = cols 
        self._hall_no = hall_no  
        self.__seats=[[0 for y in range(rows)] for x in range(cols)] 

    def get_show_list(self):
        return self.__show_list
    
    def entry_show(self,id,movie_name,time):
        self.__show_list.append((id,movie_name,time))

    def book_seats(self,show_id,bookedseat):
        for show in self.__show_list:
            if show[0] == show_id:
                row,cols=bookedseat

                if row>self.__rows and cols>self.__cols:
                    print(f"Seat ({row},{cols}) does not exist.")
                elif row<=self.__rows and cols<=self.__cols and self.__seats[row-1][cols-1] == 0:
                    self.__seats[row-1][cols-1] = 1   
                    print(f"Seat ({row},{cols}) booked for show {show_id}.")
                else:
                        print(f"Seat ({row},{cols}) is already booked")
                break

    def view_show_list(self):
        for show in self.__show_list:
            show_id, show_name,show_time = show
            print(f"MOVIE NAME: {show_name}({show_id}) SHOW ID: {show_id} TIME: {show_time}")

    def view_available_seats(self, show_id):
        print(f"Available Seats for Show {show_id}:")
        for row in self.__seats:
            for cols in row:
                print(cols,end=" ")
            print()


class Counter(Star_Cinema):
    def __init__(self):
        self.cinema = Star_Cinema
        while(True):
            print("1. VIEW ALL SHOW TODAY")
            print("2. VIEW AVAILABLE SEATS")
            print("3. BOOK TICKET")
            print("4. EXIT")
            print("ENTER OPTION: ",end=" ")
            inpt=int(input())

            if inpt==1:
                self.view_all_shows()
            elif inpt==2:
                print("ENTER SHOW ID: ",end=" ")
                idd=int(input())
                self.view_available_seats_in_show(idd)
            elif inpt==3:
                print("ENTER SHOW ID: ",end=" ")
                id_inpt=int(input())
                print("NUMBER OF TICKETS: ",end=" ")
                tic_inpt=int(input())
                for i in range(tic_inpt):
                    print("ENTER SEAT ROW: ",end=' ')
                    row_inpt=int(input())
                    print("ENTER SEAT COLUMN: ",end=' ')
                    col_input=int(input())
                    self.book_tickets(id_inpt,(row_inpt,col_input))
            elif inpt==4:
                break
            else:
                print("CHOOSE RIGHT OPTION!!!")


    def view_all_shows(self):
        print("Shows Running in the Cinema:")
        for hall in self.cinema.get_hall_list():
            hall.view_show_list()

    def view_available_seats_in_show(self, show_id):
        for hall in self.cinema.get_hall_list():
            flag=False
            for show in hall.get_show_list():
                if show[0]==show_id:
                    hall.view_available_seats(show_id)
                    flag=True
                    break
            if flag==True:
                break
        else:
            print(f"Show id {show_id} not found.")

    def book_tickets(self,  show_id, seats_to_book):
        for hall in self.cinema.get_hall_list():
            flag=False
            for show in hall.get_show_list():
                if show[0]==show_id:
                    hall.book_seats(show_id,seats_to_book)
                    flag=True
                    break
            if flag==True:
                break


Star_cineplex=Star_Cinema()

hall1 = Hall(5, 7, 1)
hall1.entry_show(1, "Jawan", "10:00 AM")
hall1.entry_show(2, "Antorjal", "2:00 PM")

hall2 = Hall(6, 8, 2)
hall2.entry_show(3, "Pathan", "5:00 PM")

hall3 = Hall(7,5, 2)
hall3.entry_show(4, "Tiger 3", "1:00 PM")

Star_cineplex.entry_hall(hall1)
Star_cineplex.entry_hall(hall2)
Star_cineplex.entry_hall(hall3)

counter= Counter()