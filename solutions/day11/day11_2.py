import re

class Monkey:
    def __init__(self, num, starting, operation, divisability, true, false):
        self.num = num
        self.starting = starting
        self.operation = operation 
        self.div = divisability
        self.true = true
        self.false = false

    def inspectItem(self, allMonkey, count, div):
        if self.num not in count:
            count[self.num] = 1
        else:
            count[self.num] += 1
        curr = self.starting.pop(0)
        curr = self.doOperation(curr)
        curr = curr % div
        if self.testDivisible(curr):
            self.giveItem(allMonkey[self.true], curr)
        else:
            self.giveItem(allMonkey[self.false], curr)
        
    
    def doOperation(self, worry):
        old = worry
        return eval(self.operation) 

    def testDivisible(self, worry):
        return worry % self.div == 0

    def acceptItem(self, worry):
        self.starting.append(worry)

    def giveItem(self, monkey, worry):
        monkey.acceptItem(worry)

    def inspectAll(self, allMonkey, count, div):
        while len(self.starting) != 0:
            self.inspectItem(allMonkey, count, div)

    def getDivisibility(self):
        return self.div

def parseMonkey(monkeyStr, num):
    startingItem = monkeyStr[1][18:].split(", ")
    startingItem = [int(i) for i in startingItem]
    operation = monkeyStr[2].split(" = ")[1]
    div = int(re.sub("[^0-9]", "", monkeyStr[3]))
    trueMonkey = int(re.sub("[^0-9]", "", monkeyStr[4]))
    falseMonkey = int(re.sub("[^0-9]", "", monkeyStr[5]))

    return Monkey(num, startingItem, operation, div, trueMonkey, falseMonkey)

def main():
    filename = "input.txt"
    allMonkey = []
    monkey = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if line != "":
                monkey.append(line)
            else:
                num = len(allMonkey)
                allMonkey.append(parseMonkey(monkey, num))
                monkey = []
        num = len(allMonkey)
        allMonkey.append(parseMonkey(monkey, num))

    div = 1
    for monkey in allMonkey:
        div *= monkey.getDivisibility()

    count = {}
    for i in range(10000):
        for monkey in allMonkey:
            monkey.inspectAll(allMonkey, count, div)

    counts = list(count.values())
    counts.sort(reverse = True)
    print(counts[0] * counts[1])


if __name__ == "__main__":
    main()





















