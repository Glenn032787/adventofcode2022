
def openFile(filename):
    result = []
    maxY = float("-inf")
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            line = line.split(" -> ")
            subList = []
            for i in line:
                x, y = i.split(",")
                if int(y)> maxY:
                    maxY = int(y)
                subList.append((int(x), int(y)))
            result.append(subList)
    return result, maxY

def getRockPath(knownRock, path):
    i = 0
    while i < len(path) - 1:
        startX, startY = path[i]
        endX, endY = path[i+1]
        knownRock.add((startX, startY))
        knownRock.add((endX, endY))

        if startX == endX:
            while startY != endY:
                if startY > endY:
                    startY -= 1
                else:
                    startY += 1
                knownRock.add((startX, startY))
        else:
            while startX != endX:
                if startX > endX:
                    startX -= 1
                else:
                    startX += 1
                knownRock.add((startX, startY))
        i += 1
    return knownRock 
        

def simulation(start, maxY, knownRock):
    current = start
    numRock = 0
    while True: # New sand
        numRock += 1
        while True: # Next movement
            X, Y = current
            
            if Y > maxY: # Sand reaches very bottom
                return numRock - 1

            if (X, Y+1) not in knownRock: # Sand fall vertically down
                current = (X, Y+1)
            elif (X-1, Y+1) not in knownRock: # Sand fall diagonally left
                current = (X-1, Y+1)
            elif (X+1, Y+1) not in knownRock: # Sand fall diagonally right
                current = (X+1, Y+1)                
            else:
                knownRock.add(current) # Sand stop falling
                current = start # New sand falls
                break



def main():
    filename = "test.txt"
    paths, maxY = openFile(filename)
    rockTiles = set()
    for path in paths:
        rockTiles = getRockPath(rockTiles, path)

    startSand = (500,0)
    result = simulation(startSand, maxY, rockTiles)
    print(result)

if __name__ == "__main__":
    main()
