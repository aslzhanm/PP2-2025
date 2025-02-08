import math

class Point:
    def __init__(self, x, y):
        self.x = x  
        self.y = y 
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x  
        self.y = y 
        print(f"Point moved to ({self.x}, {self.y})")

    def dist(self, other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        print(f"Distance to point ({other.x}, {other.y}): {distance}")
        return distance


p1 = Point(3, 4)
p2 = Point(7, 1)

p1.show()          
p2.show()          
p1.move(5, 6)     
p1.dist(p2)       