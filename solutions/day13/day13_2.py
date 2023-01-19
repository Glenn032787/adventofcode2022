from day13_1 import compareVal
import json

def sortPacket(packets):
    sortList = packets.copy()

    i = 0
    while True:
        fixed = True
        for i in range(len(sortList) - 1):
            if compareVal(sortList[i], sortList[i + 1]) == "wrong":
                sortList[i], sortList[i + 1] = sortList[i + 1], sortList[i]
                fixed = False
        if fixed:
            return sortList


def main():
    filename = "input.txt"
    
    packets = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if line != "":
                line = json.loads(line)
                packets.append(line)
    
    packets.append([[2]])
    packets.append([[6]])
    sortedPackets = sortPacket(packets)
    print(sortedPackets)
    i1 = sortedPackets.index([[2]]) + 1
    i2 = sortedPackets.index([[6]]) + 1
    print(i1 * i2)

if __name__ == "__main__":
    main()
