# Question 23
from Question_19 import Point

class Polygon:

    def __init__(self, points = [ ]):
        self.Points = points

    @staticmethod
    def findDistance(a,b):
        x = (a.x - b.x)**2
        y = (a.y - b.y)**2
        return round(((x + y)**(1/2)),2)
    
    def addPoint(self):
        x = int(input("Enter x-coordinate: "))
        y = int(input("Enter y-coordinate: "))
        P = Point(x,y)
        self.Points.append(P)

    def perimeter(self):
        Sum = 0
        for i in range(1, len(self.Points)):
            for j in range(-len(self.Points) + i, 0):
                a = self.findDistance(self.Points[ i-1 ], self.Points[ j ])
                Sum += a
        return Sum

P1 = Point(1,1)
P2 = Point(1,2)
P3 = Point(2,2)
P4 = Point(2,1)

P = Polygon([P1,P2,P3,P4])

