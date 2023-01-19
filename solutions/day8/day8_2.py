from day8_1 import importGrid, getTree

def getViewability(treeLine, curr_tree):
    i = 0
    for tree in treeLine:
        i += 1
        if tree >= curr_tree:
            break
    return i

def main():
    filename = "input.txt"
    grid = importGrid(filename)

    nrow = len(grid)
    ncol = len(grid[0])

    largestVisablity = float("-inf")

    for x in range(ncol):
        for y in range(nrow):
            curr_tree = int(grid[y][x])
            
            viewability = 1
            for direction in ["left", "right", "up", "down"]:
                treeLine = getTree(x, y, grid, direction)
                treeLine = [int(d) for d in str(treeLine)]
                score = getViewability(treeLine, curr_tree)
                viewability = viewability * score
            if viewability > largestVisablity:
                largestVisablity = viewability


    print(largestVisablity)

if __name__ == "__main__":
    main()
