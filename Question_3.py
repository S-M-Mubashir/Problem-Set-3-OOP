# Question 3
from Question_2 import Publication

class Sales:
    record = [0.0,0.0,0.0]

    def get_data(self):
        self.record[0] = float(input("Enter sales of publication of first month: "))
        self.record[1] = float(input("Enter sales of publication of second month: "))
        self.record[2] = float(input("Enter sales of publication of third month: "))

    def put_data(self):
        return f"Record of Publications: \nFirst Month: {self.record[0]} \nSecond Month: {self.record[1]} \nThird Month: {self.record[2]}"


class Book(Publication, Sales):
    pageCount = 0

    def get_data(self):
        super().get_data()
        count = int(input("Enter page count of the book: "))
        self.pageCount = count
        Sales.get_data(self)
        
    def put_data(self):
        return f"{super().put_data()} \nPage Count: {self.pageCount} \n{Sales.put_data(self)}"
        
class Tape(Publication, Sales):
    playingTime = 0.0

    def get_data(self):
        super().get_data()
        time = float(input("Enter the playing time: "))
        self.playingTime = time
        Sales.get_data(self)
        
    def put_data(self):
        return f"{super().put_data()} \nPlaying Time: {self.playingTime} \n{Sales.put_data(self)}"

##B = Book()
##B.get_data()
##print(B.put_data())
##
##print("-"*100)
##
##T = Tape()
##T.get_data()
##print(T.put_data())
