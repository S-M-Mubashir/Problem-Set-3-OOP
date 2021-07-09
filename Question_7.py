# Question 7
# Modifying Question 6
class Date:
    date = None
    month = None
    year = None
    lst = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

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
        print(''' In which format you want date to be printed:
1.) dd-mm-yy
2.) mm/dd/yy
3.) mm_name dd yy''')
        format = int(input("Enter format choice number: "))
        if format == 1:
            return f"{self.date:02} - {self.month:02} -  {self.year:02}"
        if format == 2:
            return f"{self.month:02}/{self.date:02}/{self.year:02}"
        if format == 3:
            return f"{Date.lst[self.month - 1]} {self.date:02},{self.year}."

##D = Date()
##D.set_date()
##D.set_month()
##D.set_year()
##print(D)
