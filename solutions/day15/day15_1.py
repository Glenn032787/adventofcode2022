
def manhattanDistance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

def getCoverage(sensor, distance, coveredRegion, yLevel):
    X, Y = sensor
    for i in range(distance + 1):
        for j in range(distance - i + 1):
            if (Y-j) == yLevel:
                coveredRegion.add((X - i, Y - j))
            if (Y+j) == yLevel:
                coveredRegion.add((X - i, Y + j))
            if (Y-j) == yLevel:
                coveredRegion.add((X + i, Y - j))
            if (Y+j) == yLevel:
                coveredRegion.add((X + i, Y + j))
    return coveredRegion


def distanceToY(sensor, distance, yLevel):
    X, Y = sensor
    yLevelPoint = (X, yLevel) 
    return manhattanDistance(sensor, yLevelPoint) <= distance


def parseInstruction(instruction):
    sensor, beacon = instruction.split(": ")
    
    sensorX, sensorY = sensor.split(", y=")
    _, sensorX = sensorX.split("=")

    beaconX, beaconY = beacon.split(", y=")
    _, beaconX = beaconX.split("=")

    return (int(sensorX), int(sensorY)), (int(beaconX), int(beaconY))

def getCoverageOnLevel(sensor, distance, yLevel, coverRegion):
    X, Y = sensor
    diff = abs(yLevel - Y)
    extra = distance - diff
    for i in range(extra + 1):
        coverRegion.add((X-i, yLevel))
        coverRegion.add((X+i, yLevel))
    return coverRegion



def main():
    coveredRegion = set()
    yLevel = 2000000
    filename = "input.txt"
    allBeacon = set()

    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            sensor, beacon = parseInstruction(line)
            allBeacon.add(beacon)
            distance = manhattanDistance(sensor, beacon)
            if distanceToY(sensor, distance, yLevel):
               coveredRegion = getCoverageOnLevel(sensor, distance, yLevel, coveredRegion) 
    coveredRegion = coveredRegion - allBeacon
    result = len(coveredRegion)
    print(result)

    

if __name__ == "__main__":
    main()
