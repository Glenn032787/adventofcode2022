from day14_1 import openFile, getRockPath

        
def simulation(start, maxY, knownRock):
    current = start
    numRock = 0
    while True: # New sand
        numRock += 1
        while True: # Next movement
            X, Y = current
            
            if (Y + 1) == (maxY + 2): # Sand hit floor
                knownRock.add(current)
                current = start   
                break    
            elif (X, Y+1) not in knownRock: # Sand fall vertically down
                current = (X, Y+1)
            elif (X-1, Y+1) not in knownRock: # Sand fall diagonally left
                current = (X-1, Y+1)
            elif (X+1, Y+1) not in knownRock: # Sand fall diagonally right
                current = (X+1, Y+1)         
            else:
                if current == start:
                    return numRock 
                knownRock.add(current) # Sand stop falling
                current = start # New sand falls
                break



def main():
    filename = "input.txt"
    paths, maxY = openFile(filename)
    rockTiles = set()
    for path in paths:
        rockTiles = getRockPath(rockTiles, path)

    startSand = (500,0)
    result = simulation(startSand, maxY, rockTiles)
    print(result)

if __name__ == "__main__":
    main()
