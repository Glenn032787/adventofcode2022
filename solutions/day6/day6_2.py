

def main():
    filename = "input.txt"
    string = ""
    with open(filename) as file:
        for line in file:
            string += line
    
    for i in range(14, len(string)):
        marker = string[i-14:i]
        if len(set(marker)) == 14:
            print(i)
            exit()

if __name__ == "__main__":
    main()
