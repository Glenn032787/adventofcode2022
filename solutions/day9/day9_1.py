
def moveHead(H, T, direction, amount, seen):
    if amount == 0:
        return H, T, seen
    
    Hx = H[0]
    Hy = H[1]

    if direction == 'R':
        Hx += 1
    elif direction == "L":
        Hx -= 1
    elif direction == "U":
        Hy += 1
    elif direction == "D":
        Hy -= 1

    newHead = [Hx, Hy]
    newTail, newSeen = moveTail(newHead, T, seen)

    return moveHead(newHead, newTail, direction, amount - 1, newSeen)

def moveTail(H, T, seen):
    if isAdjacent(H, T):
        return T, seen
    
    Hx = H[0]
    Hy = H[1]
    Tx = T[0]
    Ty = T[1]
   
    if Hy > Ty:
        Ty += 1
    elif Hy < Ty:
        Ty -= 1

    if Hx > Tx:
        Tx += 1
    elif Hx < Tx:
        Tx -= 1

    seen.add((Tx, Ty))
    return [Tx, Ty], seen
 

def isAdjacent(H, T):
    Hx = H[0]
    Hy = H[1]

    for x in [Hx - 1, Hx, Hx + 1]:
        for y in [Hy - 1, Hy, Hy + 1]:
            if T == [x, y]:
                return True
    return False


def main():
    
    H = [0,0]
    T = [0,0]

    seen = set((0,0))

    filename = "input.txt"
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            direction, amount = line.split(' ')
            amount = int(amount)
            H, T, seen = moveHead(H, T, direction, amount, seen)
    
    numSeen = len(seen)
    print(numSeen)

if __name__ == "__main__":
    main()


