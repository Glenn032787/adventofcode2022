from typing import List

def parsePair(line:str) -> List[int]:
    p1, p2 = line.split(",")
    l1, u1 = p1.split("-")
    l2, u2 = p2.split("-")
    return int(l1), int(u1), int(l2), int(u2)

def fullOverlap(l1: int, u1:int, 
                l2: int, u2: int) -> bool:
    if l1 <= l2 and u1 >= u2:
        return True
    elif l2 <= l1 and u2 >= u1:
        return True
    else:
        return False


def main():
    result = 0
    with open("input.txt", "r") as file:
        for line in file:
            line = line.rstrip()
            l1, u1, l2, u2 = parsePair(line)
            if fullOverlap(l1, u1, l2, u2):
                result += 1
    print(result)

if __name__ == "__main__":
    main()
