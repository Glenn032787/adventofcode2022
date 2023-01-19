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

def getPossibleAdjacent(grid, current):
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
        if (grid[coord[1]][coord[0]] - grid[y][x]) <= 1:
            possibleAdjacent.append(coord)
    return possibleAdjacent



class path:
    def __init__(self, coord, previous=None):
        self.previous = previous
        self.coord = coord
    
    def __str__(self):
        return self.coord
    def __repr__(self):
        return self.coord



def BFS(grid, start, end):
    queue = []
    curr = path(start)
    visited = [start] 
    while True:
        if curr.coord == end:
            return curr
        possible = getPossibleAdjacent(grid, curr.coord)
        for position in possible:
            if position in visited:
                continue
            visited.append(position)
            next_path = path(position, curr)
            queue.append(next_path)
        if len(queue) == 0:
            return None
        curr = queue.pop(0)
        


def convertGrid(grid):
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

def countSteps(path):
    count = 0
    while path.previous != None:
        count += 1
        path = path.previous
    return count

def main():
    filename = "input.txt"
    grid = getGrid(filename)
    start, end = getStartEndCoord(grid)
    grid = convertGrid(grid)
    curr = BFS(grid, start, end)
    steps = countSteps(curr)
    print(steps)
    


if __name__ == "__main__":
    main()
