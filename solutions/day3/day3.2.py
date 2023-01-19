from day3_1 import getScore  

def getSim(w1, w2, w3):
    a = set(w1)
    b = set(w2)
    c = set(w3)
    intersect = a.intersection(b, c)
    return list(intersect)[0]



def main():
    filename = "input.txt"
    result = 0

    with open(filename) as file:
        fileList = file.readlines()
        i = 0
        while i < len(fileList):
            l1 = fileList[i].rstrip()
            l2 = fileList[i+1].rstrip()
            l3 = fileList[i+2].rstrip()
            i = i + 3
            badge = getSim(l1, l2, l3)
            result += getScore(badge)


    print(result)

if __name__ == "__main__":
    main()

