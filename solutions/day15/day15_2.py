from day15_1 import manhattanDistance, parseInstruction

def perimeter(sensor, distance, known, maxVal):
    X, Y = sensor
    for i in range(distance + 1):
        length = distance - i
        currY1 = Y - i
        currY2 = Y + i

        currX1 = max(0, X-length)
        currX1 = min(maxVal, currX1)

        currX2 = max(0, X+length)
        currX2 = min(maxVal, currX2)
        
        if currY1 >= 0 and currY1 <= maxVal:
            if currY1 in known:
                known[currY1].add((currX1, currX2))
            else:
                known[currY1] = {(currX1, currX2)}

        if currY2 >= 0 and currY2 <= maxVal:
            if currY2 in known:
                known[currY2].add((currX1, currX2))
            else:
                known[currY2] = {(currX1, currX2)}
    return known

def isLine(points, maxVal):
    pointList = list(points)
    pointList.sort()
    minimum, maximum = pointList[0]
    if minimum != 0:
        return False

    i = 1
    while i < len(pointList):
        X, Y = pointList[i]
        if X - maximum > 1:
            return False
        else:
            maximum = max(Y, maximum)
        i += 1
    return maximum == maxVal

def simplify(points):
    pointList = list(points)
    pointList.sort()
    minimum, maximum = pointList[0]
    i = 1
    while i < len(pointList):
        X, Y = pointList[i]
        if X - maximum > 1:
            return maximum + 1
        else:
            maximum = max(Y, maximum)
        i += 1
    return -1

def main():
    filename = "input.txt"
    maxDistance = 4000000
    known = {}
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            sensor, beacon = parseInstruction(line)
            distance = manhattanDistance(sensor, beacon)
            known = perimeter(sensor, distance, known, maxDistance)
    for Y in known:
        if not isLine(known[Y], maxDistance):
            X = simplify(known[Y])
            print((X * 4000000) + Y)
if __name__ == "__main__":
    main()
