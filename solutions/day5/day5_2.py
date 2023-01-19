from day5_1 import parseInput, parseCrate, parseInstruction


def moveCrate(crate, num, origin, destination):
    move = crate[origin - 1][:num]
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
