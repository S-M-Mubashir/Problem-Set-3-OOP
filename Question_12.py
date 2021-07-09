# Question 12
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

E = Engine("xyz122", "23/5/2020")
V = Vehicle(8, "Red", "123AS", E)
print(V.get_wheels())
print(V.get_color())
print(V.get_model())
print(V.Engine.get_engineNo())
print(V.Engine.get_date())
