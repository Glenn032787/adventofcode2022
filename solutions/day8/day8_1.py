from typing import List 

def importGrid(filename: str) -> List[str]:
    grid = []
    with open(filename) as file:
        for line in file:
           line = line.rstrip()
           grid.append(line)
    return grid

def getTree(x, y, grid, direction):
    assert direction in ["left", "right", "up", "down"]
    
    if direction == "left":
        return grid[y][:x][::-1]
    elif direction == "right":
        return grid[y][x+1:]
   
    tree = ""
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if i == x:
                tree += grid[j][i]

    if direction == "up":
        return tree[:y][::-1]
    elif direction == "down":
        return tree[y+1:]

    
def isVisable(allTree, currTree):
    for tree in allTree:
        if tree >= currTree:
            return False
    return True

def main():
    filename = "input.txt"
    grid = importGrid(filename)

    nrow = len(grid)
    ncol = len(grid[0])
    
    visable = 0

    for x in range(ncol):
        for y in range(nrow):
            if x == 0 or x == ncol - 1 or y == 0 or y == nrow - 1:
                # Edge trees are always visable
                visable += 1
                continue
            curr_tree = int(grid[y][x])
            
            for direction in ["left", "right", "up", "down"]:
                treeLine = getTree(x, y, grid, direction)
                treeLine = [int(d) for d in str(treeLine)]
                if isVisable(treeLine, curr_tree):
                    visable += 1
                    break
    print(visable)

if __name__ == "__main__":
    main() 

    
