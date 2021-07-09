# Question 2
class Publication:
    title = " "
    price = 0.0
    
    def get_data(self):
        t = input("Enter title of the book: ")
        self.title = t
        p = float(input("Enter price of the book: "))
        self.price = p

    def put_data(self):
        return f"Title: {self.title} \nPrice: {self.price}"

class Book(Publication):
    pageCount = 0
    
    def get_data(self):
        super().get_data()
        count = int(input("Enter page count: "))
        self.pageCount = count
    def put_data(self):
        return f"{super().put_data()} \nPage Count: {self.pageCount}"

class Tape(Publication):
    playingTime = 0.0
    
    def get_data(self):
        super().get_data()
        time = float(input("Enter time: "))
        self.playingTime = time
    def put_data(self):
        return f"{super().put_data()} \nPlaying Time: {self.playingTime}"

# Comment out the driver code cz have imported classes in different questions

##B = Book()
##B.get_data()
##print(B.put_data())
##
##print("-"*100)
##
##T = Tape()
##T.get_data()
##print(T.put_data())
