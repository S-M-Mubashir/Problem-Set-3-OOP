# Quesiton 21
from Question_19 import Point

class Distance:

    def __init__(self, x1,y1, x2,y2):            
        self.p1 = Point(x1,y1)
        self.p2 = Point(x2,y2)
        
    def set_objects(self):
        x1 = int(input("Enter x for point 1: "))
        y1 = int(input("Enter y for point 1 : "))
        x2 = int(input("Enter x for point 2: "))
        y2 = int(input("Enter y for point 2 : "))
        self.p1 = Point(x1,y1)
        self.p2 = Point(x2,y2)
        
    def findDistance(self):
        x = (self.p1.x - self.p2.x)**2
        y = (self.p1.y - self.p2.y)**2
        self.distance = round(((x + y)**(1/2)),2)
        return self.distance

    def __sub__(self,D):
        if self.distance > D.distance:
            return self.distance - D.distance
        else:
            return "First Distance should be greater than the Second Distance \nNo negative distances allowed"
        

D1 = Distance(9,2,0,4)
D2 = Distance(7,5,1,2)

D1.findDistance()
D2.findDistance()

print(D1 - D2)
