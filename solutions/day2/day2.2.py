
result = {"X": 0, "Y": 3, "Z": 6}
win_condition = {"A": 2, "B": 3, "C": 1}
lose_condition = {"A": 3, "B": 1, "C": 2}
tie_condition = {"A": 1, "B": 2, "C": 3}

total = 0

filename = "input.txt"


with open(filename) as file:
    for line in file:
        line = line.rstrip()
        val = tuple(line.split(' '))
        
        condition = val[1]
        score = result[condition]
        if condition == "X":
            score += lose_condition[val[0]]
        elif condition == "Y":
            score += tie_condition[val[0]]
        else:
            score += win_condition[val[0]]
        total += score


print(total)
