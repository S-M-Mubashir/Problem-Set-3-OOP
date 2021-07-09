# Question 6
class Date:
    date = None
    month = None
    year = None

    def set_date(self):
        self.date = int(input("Enter date: "))
    def get_date(self):
        return self.date
    
    def set_month(self):
        self.month = int(input("Enter month: "))
    def get_month(self):
        return self.month

    def set_year(self):
        self.year = int(input("Enter year: "))
    def get_year(self):
        return self.year

    def __str__(self):
        return f"{(self.date):02} - {(self.month):02} - {(self.year)}"

##D = Date()
##D.set_date()
##D.set_month()
##D.set_year()
##print(D)


