from day4_1 import parsePair, fullOverlap


def checkOverlap(l1: int, u1: int,
                l2: int, u2: int) -> bool:
    if l2 >= l1 and l2 <= u1:
        return True
    elif u2 >= l1 and u2 <= u1:
        return True
    else:
        return False

def main():
    filename = "input.txt"
    count = 0
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            l1, u1, l2, u2 = parsePair(line)
            if fullOverlap(l1, u1, l2, u2):
                count += 1
            elif checkOverlap(l1, u1, l2, u2):
                count += 1
    print(count)

if __name__ == "__main__":
    main()

