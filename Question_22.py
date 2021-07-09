# Question 22

class DistanceFinder:
    def findDistance(self, p):
        if type(p) == Point:
            x = (self.x - p.x)**2
            y = (self.y - p.y)**2
            return round(((x + y)**(1/2)),2)


class Point(DistanceFinder):

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def set_points(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

P1 = Point(4,5)
P2 = Point(6,7)

print(P1.findDistance(P2))
