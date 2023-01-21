from copy import deepcopy
import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer

from set import Set
from point import Point

def classify(x, y, k, vicinity):
    for point in vicinity:
        point.calculateDistance(x, y)
    vicinity.sort(key=lambda el: el.distanceFromNewPoint)
    freq = [0,0,0,0]
    for p in range(k):
        freq[vicinity[p].color] += 1
    return freq.index(max(freq))

def generateCoords(pointType):
    percentageOfPointsoGeneratedInItsSquare = 0.99
    percentageOfPointsGeneratedInGivenArea = random.random()
    if percentageOfPointsGeneratedInGivenArea <= percentageOfPointsoGeneratedInItsSquare:
        match pointType:
            case 0:
                return (random.randint(-5000, 499), random.randint(-5000, 499))
            case 1:
                return (random.randint(-499, 5000), random.randint(-5000, 499))
            case 2:
                return (random.randint(-5000, 499), random.randint(-499, 5000))
            case 3:
                return (random.randint(-499, 5000), random.randint(-499, 5000))
    return (random.randint(-5000, 5000), random.randint(-5000, 5000))

def generateNewPoints(setOfPoints):
    numPointsOfEachTypeLeft = 1000 # pocet bodov pre kazdu kategoriu
    while(numPointsOfEachTypeLeft):
        for color in range(4):
            while(True):
                x, y = generateCoords(color)
                if (not setOfPoints.hasPoint(x, y)):
                    setOfPoints.storePoint(x, y)
                    setOfPoints.addNewPoint(Point(x, y, color))
                    break
        numPointsOfEachTypeLeft -= 1

def initialize(setOfPoints):
    numOfPointsOfGivenType = 5
    red_initial = [(-4500, -4400), (-4100, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)]
    green_initial = [(4500, -4400), (4100, -3000), (1800, -2400), (2500, -3400), (2000, -1400)]
    blue_initial = [(-4500, 4400), (-4100, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)]
    purple_initial = [(4500, 4400), (4100, 3000), (1800, 2400), (2500, 3400), (2000, 1400)]
    for pointIndex in range(numOfPointsOfGivenType):
        setOfPoints.storePoint(red_initial[pointIndex][0], red_initial[pointIndex][1])
        setOfPoints.storePoint(green_initial[pointIndex][0], green_initial[pointIndex][1])
        setOfPoints.storePoint(blue_initial[pointIndex][0], blue_initial[pointIndex][1])
        setOfPoints.storePoint(purple_initial[pointIndex][0], purple_initial[pointIndex][1])

        setOfPoints.addInitialPoint(Point(red_initial[pointIndex][0], red_initial[pointIndex][1], 0))
        setOfPoints.addInitialPoint(Point(green_initial[pointIndex][0], green_initial[pointIndex][1], 1))
        setOfPoints.addInitialPoint(Point(blue_initial[pointIndex][0], blue_initial[pointIndex][1], 2))
        setOfPoints.addInitialPoint(Point(purple_initial[pointIndex][0], purple_initial[pointIndex][1], 3))

def storeCoords(point, rx, ry, gx, gy, bx, by, px, py):
    match point.color:
        case 0:
            rx.append(point.x)
            ry.append(point.y)
        case 1:
            gx.append(point.x)
            gy.append(point.y)
        case 2:
            bx.append(point.x)
            by.append(point.y)
        case 3:
            px.append(point.x)
            py.append(point.y)

def testing(setOfPoints, k):
 
    rx = list()
    ry = list()
    gx = list()
    gy = list()
    bx = list()
    by = list()
    px = list()
    py = list()

    processedPoints = list()
    processedPoints = deepcopy(setOfPoints.initialPoints)
    for initPoint in setOfPoints.initialPoints:
        storeCoords(initPoint, rx, ry, gx, gy, bx, by, px, py)
    numOfNewPoints = 0
    numOfCorrectlyClassifiedPoints = 0
    prevPoint = 0
    t1 = timer()
    for newPoint in setOfPoints.newPoints:
        assignedType = classify(newPoint.x, newPoint.y, k, processedPoints)
        if (assignedType == newPoint.color):
            numOfCorrectlyClassifiedPoints += 1
        numOfNewPoints += 1
        p = deepcopy(newPoint)
        p.color = assignedType
        processedPoints.append(p)
        
        if prevPoint != 0:
            storeCoords(prevPoint, rx, ry, gx, gy, bx, by, px, py)
        prevPoint = p
        lx = list()
        lx.append(p.x)
        ly = list()
        ly.append(p.y)
    t2 = timer()
    print("k = ", k)
    print("uspesnost: ", numOfCorrectlyClassifiedPoints / numOfNewPoints * 100)
    print("cas vykonania: ", (t2-t1))
    storeCoords(prevPoint, rx, ry, gx, gy, bx, by, px, py)
    
    ax = plt.subplot()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.scatter(rx, ry, color="red")
    plt.scatter(gx, gy, color="green")
    plt.scatter(bx, by, color="blue")
    plt.scatter(px, py, color="purple")
    #plt.scatter(lx, ly, color="black")
    plt.title(f'k = {k}')
    plt.show()
        


def main():
    setOfPoints = Set()

    initialize(setOfPoints)
    generateNewPoints(setOfPoints)
    k = [1, 3, 7, 15]
    for i in k:
        testing(setOfPoints, i)
    print("fin")

main()