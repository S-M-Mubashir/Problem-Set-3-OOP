# Quesiton 9
# Modifying Question 8 to add count
from Question_7 import Date

# By composition

class Publication:
    title = " "
    price = 0.0

    def __init__(self):
        self.Date = Date()
        
    def get_data(self):
        t = input("Enter title of the book: ")
        self.title = t
        p = float(input("Enter price of the book: "))
        self.price = p
        self.Date.set_date()
        self.Date.set_month()
        self.Date.set_year()

    def put_data(self):
        date = self.Date
        return f"Title: {self.title} \nPrice: {self.price} \nDate of Publication: {date}"
    
class Book(Publication):
    pageCount = 0
    count = 0

    def __init__(self):
        super().__init__()
        Book.count += 1
        self.count_book = Book.count
        
    def get_data(self):
        super().get_data()
        count = int(input("Enter page count of the book: "))
        self.pageCount = count
        
    def put_data(self):
        return f"{super().put_data()} \nPage Count: {self.pageCount} \nObject Number: {self.count_book}"
        
class Tape(Publication):
    playingTime = 0.0
    count = 0

    def __init__(self):
        super().__init__()
        Tape.count += 1
        self.count_tape = Tape.count
        
    def get_data(self):
        super().get_data()
        time = float(input("Enter the playing time: "))
        self.playingTime = time
        
    def put_data(self):
        return f"{super().put_data()} \nPlaying Time: {self.playingTime} \nObject Number: {self.count_tape}"

##B = Book()
##B.get_data()
##print(B.put_data())
##
##print("-"*100)
##
##T = Tape()
##T.get_data()
##print(T.put_data())


# By aggregation

class Publication:
    title = " "
    price = 0.0

    def __init__(self,D):
        if type(D) == Date:
            self.Date = D
        
    def get_data(self):
        t = input("Enter title of the book: ")
        self.title = t
        p = float(input("Enter price of the book: "))
        self.price = p
        self.Date.set_date()
        self.Date.set_month()
        self.Date.set_year()

    def put_data(self):
        date = self.Date
        return f"Title: {self.title} \nPrice: {self.price} \nDate of Publication: {date}"
    
class Book(Publication):
    pageCount = 0
    count = 0

    def __init__(self, D):
        super().__init__(D)
        Book.count += 1
        self.count_book = Book.count
        
    def get_data(self):
        super().get_data()
        count = int(input("Enter page count of the book: "))
        self.pageCount = count
        
    def put_data(self):
        return f"{super().put_data()} \nPage Count: {self.pageCount} \nObject Number: {self.count_book}"
        
class Tape(Publication):
    playingTime = 0.0
    count = 0

    def __init__(self,D):
        super().__init__(D)
        Tape.count += 1
        self.count_tape = Tape.count
        
    def get_data(self):
        super().get_data()
        time = float(input("Enter the playing time: "))
        self.playingTime = time
        
    def put_data(self):
        return f"{super().put_data()} \nPlaying Time: {self.playingTime} \nObject Number: {self.count_tape}"

##D = Date()
##
##B = Book(D)
##B.get_data()
##print(B.put_data())
##
##print("-"*100)
##
##T = Tape(D)
##T.get_data()
##print(T.put_data())
