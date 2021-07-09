# Question 11
class Vehicle:

    def __init__(self, wheels = 4, color  = "Blue", model = "XYZ"):
        self.__noOfWheels = wheels
        self.__color = color
        self.__modelNo = model

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

##V = Vehicle()
##V.set_wheels(4)
##V.set_color("Red")
##V.set_model("HWP")
