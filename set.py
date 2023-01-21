
class Set:
    def __init__(self):
        self.area = [[0 for x in range(10001)] for y in range(10001)]
        self.newPoints = list()
        self.initialPoints = list()
    
    def storePoint(self, x, y):
        row = y + 5000
        column = x + 5000
        self.area[row][column] = 1
    
    def hasPoint(self, x, y):
        row = y + 5000
        column = x + 5000
        if (self.area[row][column] == 1):
            return True
        return False
    
    def addNewPoint(self, point):
        self.newPoints.append(point)

    def addInitialPoint(self, point):
        self.initialPoints.append(point)


