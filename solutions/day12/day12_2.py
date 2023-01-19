from day12_1 import *

def getStartEndCoord(grid):
    start = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start.append((x, y))
            elif grid[y][x] == "a":
                start.append((x, y))
            elif grid[y][x] == "E":
                end = (x, y)
    return start, end


def main():
    filename = "input.txt"
    grid = getGrid(filename)
    start, end = getStartEndCoord(grid)
    grid = convertGrid(grid)
    
    minStep = float("inf")
    for startPath in start:
        curr = BFS(grid, startPath, end)
        if curr == None:
            continue
        steps = countSteps(curr)
        if steps < minStep:
            minStep = steps
    print(minStep)

if __name__ == "__main__":
    main()
