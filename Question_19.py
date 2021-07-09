# Question 19
class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def set_points(self):
        self.x = int(input("Enter x-coordinate: "))
        self.y = int(input("Enter y-coordinate: "))

    def __str__(self):
        return f"({self.x},{self.y})"

##P1 = Point(1,3)
##P2 = Point(4,-6)
##
##print(P1)
##print(P2)
