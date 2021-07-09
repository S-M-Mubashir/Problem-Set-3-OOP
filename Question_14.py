# Question 14
# adding __str__ in code of Question 12
class Engine:

    def __init__(self, engine = "xyz", date = "00-00-00"):
        self.__engineNo = engine
        self.__dateOfManufacture = date

    def set_engineNo(self,e):
        self.__engineNo = e
    def get_engineNo(self):
        return self.__engineNo

    def set_date(self,date):
        self.__dateOfManufacture = date
    def get_date(self):
        return self.__dateOfManufacture

class Vehicle:

    def __init__(self, wheels = 4, color  = "Blue", model = "XYZ", engine = None):
        self.__noOfWheels = wheels
        self.__color = color
        self.__modelNo = model
        if type(engine) == Engine:
            self.Engine = engine

    def set_wheels(self,w):
        self.__noOfWheels = w
    def get_wheels(self):
        return self.__noOfWheels

    def set_color(self,c):
        self.__color = c
    def get_color(self):
        return self.__color

    def set_model(self,m):
        self.__modelNo = m
    def get_model(self):
        return self.__modelNo

    def __str__(self):
        return f"Class Vehicle \nModel no.:{self.get_model()} \nNo of wheels: {self.get_wheels()} \nEngine no: {self.Engine.get_engineNo()} \nDate of manufacture (engine): {self.Engine.get_date()}"

E = Engine("xyz122", "23/5/2020")
V = Vehicle(8, "Red", "123AS", E)
print(V)
