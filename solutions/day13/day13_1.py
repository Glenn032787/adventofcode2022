import json 

def compareVal(left, right):
    c1 = type(left)
    c2 = type(right)

    if c1 == int and c2 == int:
        if left < right:
            return "right"
        elif right < left:
            return "wrong"
        else:
            return "next"
    elif c1 == list and c2 == list:
        i = 0
        while True:
            if len(left) != len(right):
                if i >= len(left):
                    return "right"
                elif i >= len(right):
                    return "wrong"
            else:
                if i >= len(left):
                    return "next"

            result = compareVal(left[i], right[i])
            if result == "next":
                i += 1
                continue
            else:
                return result
    elif c1 == int and c2 == list:
        return compareVal([left], right)
    elif c1 == list and c2 == int:
        return compareVal(left, [right])

def main():
    filename = "input.txt"
    
    i = 1
    curr = []
    final = []

    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if line == "":
                result = compareVal(curr[0], curr[1])
                if result == "right":
                    final.append(i)
                curr = []
                i += 1
            else:
                listVal = json.loads(line)
                curr.append(listVal)
    indexSum = sum(final)
    print(indexSum)

if __name__ == "__main__":
    main()
    