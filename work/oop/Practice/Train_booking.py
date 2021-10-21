class train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def train_info(self):
        print("Name- {}".format(self.name), "\nFare- RS {}/- only".format(self.fare))
    def seat_info(self):
        print("No. of seats available- {}".format(self.seats))
    def book_ticket(self):
        if self.seats > 0:
            print("Your ticket has been booked. Your seat no. is {}".format(self.seats))
            self.seats -= 1
        else:
            print("Sorry, no seats available, try in tatkal")


train1 = train("Intercity Express 150036", 115, 350)
train1.train_info()
train1.seat_info()

train1.book_ticket()
train1.book_ticket()
train1.book_ticket()
train1.book_ticket()
train1.book_ticket()

train1.seat_info()


