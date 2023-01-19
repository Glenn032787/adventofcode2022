from typing import List

def parseInput(filename: str) -> List[str]:

    flip = True
    crate = []
    instruction = []
    with open(filename) as file:
        for line in file:
            if line == "\n":
                flip = not flip
            elif flip:
                crate.append(line)
            else:
                instruction.append(line)
    return crate, instruction

def parseCrate(crate):
    numRow = crate[-1].split("   ")[-1]
    numRow = int(numRow)
    result = [[] for i in range(numRow)]
    crate.pop()
    for row in crate:
        for i in range(numRow):
            if row[1+4*i] != " ":
                result[i].append(row[1+4*i])
    return result


def parseInstruction(instruction):
    instruction = instruction[4:]
    num, instruction = instruction.split(" from ")
    origin, destination = instruction.split(" to ")
    return int(num), int(origin), int(destination)
    

def moveCrate(crate, num, origin, destination):
    move = crate[origin - 1][:num]
    move.reverse()
    newOri = crate[origin - 1][num: ]
    newDes = move + crate[destination - 1]
    crate[origin - 1] = newOri
    crate[destination - 1] = newDes
    return crate

def main():
    filename = "input.txt"
    crate, instructions = parseInput(filename)
    crate = parseCrate(crate)
    for instruction in instructions:
        num, origin, destination = parseInstruction(instruction)
        crate = moveCrate(crate, num, origin, destination)
    result = ''
    for row in crate:
        result += row[0]
    print(result)
    

if __name__ == "__main__":
    main()
