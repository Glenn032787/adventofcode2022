
shape = {"X": 1, "Y": 2, "Z": 3}
win_condition = [("A", "Y"),("B", "Z"),("C", "X")]
tie_condition = [("A", "X"), ("B", "Y"), ("C", "Z")]

total = 0

filename = "input.txt"


with open(filename) as file:
    for line in file:
        line = line.rstrip()
        val = tuple(line.split(' '))
        
        curr = shape[val[1]]
        if val in win_condition:
            curr += 6
        elif val in tie_condition:
            curr += 3
        total += curr

print(total)
