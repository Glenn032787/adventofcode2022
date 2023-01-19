from typing import List

def getGrid(filename: str) -> List[str]:
    grid = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            grid.append(line)
    return grid

def getStartEndCoord(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = (x, y)
            elif grid[y][x] == "E":
                end = (x, y)
    return start, end


def getPossibleAdjacent(grid, current, visited):
    x = current[0]
    y = current[1]
    adjacent = [] 
    if x - 1 >= 0 and x - 1 < len(grid[0]):
        adjacent.append((x - 1, y))

    if x + 1 >= 0 and x + 1 < len(grid[0]):
        adjacent.append((x + 1, y))

    if y - 1 >= 0 and y - 1 < len(grid):
        adjacent.append((x, y - 1))

    if y + 1 >= 0 and y + 1 < len(grid):
        adjacent.append((x, y + 1))

    possibleAdjacent = []

    for coord in adjacent:
        if (grid[coord[1]][coord[0]] - grid[y][x]) <= 1 and coord not in visited:
            possibleAdjacent.append(coord)
    return possibleAdjacent
            


def higher(currCoord, nextCoord, grid):
    currLetter = grid[currCoord[1]][currCoord[0]]
    nextLetter = grid[nextCoord[1]][nextCoord[0]]

    if currLetter == "S":
        currOrd = ord("a")
    elif currLetter == "E":
        currOrd = ord("z")
    else:
        currOrd = ord(currLetter)

    if nextLetter == "S":
        nextOrd = ord("a")
    elif nextLetter == "E":
        nextOrd = ord("z")
    else:
        nextOrd = ord(nextLetter)

    return (nextOrd - currOrd) <= 1 





def findPath(grid, curr, end, visited, deadend = []) -> int:
    if curr == end:
        return 0 
    visited = [curr] + visited
    possibleCoord = getPossibleAdjacent(grid, curr, visited)
    if len(possibleCoord) == 0:
        deadend.append(curr)
        return -1

    possibleSteps = []
    for coord in possibleCoord:
        if coord in deadend:
            continue
        steps = findPath(grid, coord, end, visited, deadend)
        if steps == -1:
            deadend.append(coord)
            continue
        possibleSteps.append(steps + 1)
    if len(possibleSteps) == 0:
        deadend.append(curr)
        return -1
    else:
        return min(possibleSteps) 

        

def converGrid(grid):
    newGrid = [[] for i in range(len(grid))]
    for i in range(len(grid)):
        for letter in grid[i]:
            if letter != "S" and letter != "E":
                newGrid[i].append(ord(letter))
            elif letter == "S":
                newGrid[i].append(ord("a"))
            else:
                newGrid[i].append(ord("z"))
    return newGrid


def main():
    filename = "test.txt"
    grid = getGrid(filename)
    start, end = getStartEndCoord(grid)
    grid = converGrid(grid)
    step = findPath(grid, start, end, [], [])
    print(step)


if __name__ == "__main__":
    main()
