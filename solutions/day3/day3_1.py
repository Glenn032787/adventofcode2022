
def split(txt):
    mid = len(txt)//2
    return (txt[:mid], txt[mid:])

def findDiff(word1, word2):
   word1_set = set(word1)
   word2_set = set(word2)
   word = word1_set.intersection(word2_set)
   return list(word)[0]

def getScore(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96 

def main():
    filename = "input.txt"
    result = []

    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            w1, w2 = split(line)
            diff = findDiff(w1, w2)
            result.append(diff)

    score = 0
    for letter in result:
        score += getScore(letter)

    print(score)

if __name__ == "__main__":
    main()

