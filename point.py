from math import sqrt

class Point():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.distanceFromNewPoint = 0
    
    def calculateDistance(self, newPoint_x, newPoint_y):
        xDifference = self.x - newPoint_x
        yDifference = self.y - newPoint_y
        self.distanceFromNewPoint = sqrt(pow(xDifference, 2) + pow(yDifference, 2))


