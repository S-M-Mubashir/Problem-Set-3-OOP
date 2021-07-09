# Question 5
from Question_2 import Publication
from Question_3 import Sales

# for composition
class Book(Publication):
    pageCount = 0

    def __init__(self):
        self.Sales = Sales()
        
    def get_data(self):
        super().get_data()
        count = int(input("Enter page count of the book: "))
        self.pageCount = count
        self.Sales.get_data()
        
    def put_data(self):
        return f"{super().put_data()} \nPage Count: {self.pageCount} \n{self.Sales.put_data()}"
        
class Tape(Publication):
    playingTime = 0.0

    def __init__(self):
        self.Sales = Sales()
        
    def get_data(self):
        super().get_data()
        time = float(input("Enter the playing time: "))
        self.playingTime = time
        self.Sales.get_data()
        
    def put_data(self):
        return f"{super().put_data()} \nPlaying Time: {self.playingTime} \n{self.Sales.put_data()}"

##B = Book()
##B.get_data()
##print(B.put_data())
##
##print("-"*100)
##
##T = Tape()
##T.get_data()
##print(T.put_data())


# for aggregation
class Book(Publication):
    pageCount = 0

    def __init__(self, S):
        if type(S) == Sales:
            self.Sales = S
        
    def get_data(self):
        super().get_data()
        count = int(input("Enter page count of the book: "))
        self.pageCount = count
        self.Sales.get_data()
        
    def put_data(self):
        return f"{super().put_data()} \nPage Count: {self.pageCount} \n{self.Sales.put_data()}"
        
class Tape(Publication):
    playingTime = 0.0

    def __init__(self, S):
        if type(S) == Sales:
            self.Sales = S

    def get_data(self):
        super().get_data()
        time = float(input("Enter the playing time: "))
        self.playingTime = time
        self.Sales.get_data()
        
    def put_data(self):
        return f"{super().put_data()} \nPlaying Time: {self.playingTime} \n{self.Sales.put_data()}"

##S = Sales()
##B = Book(S)
##B.get_data()
##print(B.put_data())
##
##print("-"*100)
##
##T = Tape(S)
##T.get_data()
##print(T.put_data())
