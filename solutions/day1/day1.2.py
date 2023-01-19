
filename="input.txt"

curr = 0
result = []

with open(filename) as file:
    for line in file:
        line = line.rstrip()
        if line != "":
            curr += int(line)
        else:
            result.append(curr)
            curr = 0

result.sort(reverse = True)

print(sum(result[:3]))
