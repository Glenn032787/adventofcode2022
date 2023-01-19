
def moveHead(rope, direction, amount, seen):
    if amount == 0:
        return rope, seen
    
    Hx = rope[0][0]
    Hy = rope[0][1]

    if direction == 'R':
        Hx += 1
    elif direction == "L":
        Hx -= 1
    elif direction == "U":
        Hy += 1
    elif direction == "D":
        Hy -= 1

    newRope = [[Hx, Hy]] + rope[1:]
    newRope, newSeen = moveTail(newRope, 1, seen)

    return moveHead(newRope, direction, amount - 1, newSeen)

def moveTail(rope, curr, seen):
    if curr >= len(rope):
        return rope, seen

    H = rope[curr - 1]
    T = rope[curr]

    if isAdjacent(H, T):
        return rope, seen
    
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
    
    if curr == len(rope) - 1:
        seen.add((Tx, Ty))

    rope[curr] = [Tx, Ty]
    return moveTail(rope, curr + 1, seen)
 

def isAdjacent(H, T):
    Hx = H[0]
    Hy = H[1]

    for x in [Hx - 1, Hx, Hx + 1]:
        for y in [Hy - 1, Hy, Hy + 1]:
            if T == [x, y]:
                return True
    return False


def main():
    ropeLength = 10 

    rope = [[0,0] for i in range(ropeLength)] 
    seen = set((0,0))

    filename = "input.txt"
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            direction, amount = line.split(' ')
            amount = int(amount)
            rope, seen = moveHead(rope, direction, amount, seen)
    
    numSeen = len(seen)
    print(numSeen)

if __name__ == "__main__":
    main()


