

def main():
    val = 1

    filename = "input.txt"
    
    instruction = []
    with open(filename) as file:
        for line in file:
            instruction.append(line.rstrip())
    instruction = instruction[::-1]
    
    cycleOfInterest = [20, 60, 100, 140, 180, 220]

    result = 0
    
    newInstruction = True
    wait = False
    cycle = 0
    
    while len(instruction) > 0:
        cycle += 1
        if cycle in cycleOfInterest:
            result += (val * cycle)
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
         
        
    print(result)

if __name__ == "__main__":
    main()
