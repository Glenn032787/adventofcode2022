
filename="input.txt"

maximum = 0
curr = 0

with open(filename) as file:
    for line in file:
        line = line.rstrip()
        if line != "":
            curr += int(line)
        else:
            if curr > maximum:
                maximum = curr
            curr = 0

print(maximum)
