def getSignal(allSignal, score, cycle):
    row = cycle//40
    col = cycle%40
    
    if len(allSignal) <= row:
        allSignal.append("")

    if col in [score - 1, score, score + 1]:
        allSignal[row] += "#"
    else:
        allSignal[row] += "."
    return allSignal


def main():
    val = 1

    filename = "input.txt"
        
    instruction = []
    with open(filename) as file:
        for line in file:
            instruction.append(line.rstrip())
    instruction = instruction[::-1]
    
    result = []
    
    newInstruction = True
    wait = False
    cycle = 0
    
    while len(instruction) > 0:


        result = getSignal(result, val, cycle)
        cycle += 1
        if newInstruction:
            currInstruction = instruction.pop()

        if currInstruction == "noop":
            newInstruction = True
            pass
        else:
            if wait:
                wait = False
                newInstruction = True
                _, newVal = currInstruction.split(" ")
                val += int(newVal)
            else:
                wait = True
                newInstruction = False

    for row in result:
        print(row)


         
        

if __name__ == "__main__":
    main()
