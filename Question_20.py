# Question 20
from Question_19 import Point

class Distance:

    def __init__(self, x1,y1, x2,y2):            # Relation is Composition
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
        return round(((x+y) **(1/2)), 2)

##D = Distance(1,5,1,3)
##print(D.findDistance())
