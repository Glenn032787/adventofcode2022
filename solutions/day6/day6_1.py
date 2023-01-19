



def main():
    filename = "input.txt"
    string = ""
    with open(filename) as file:
        for line in file:
            string += line
    
    for i in range(4, len(string)):
        marker = string[i-4:i]
        if len(set(marker)) == 4:
            print(i)
            exit()

if __name__ == "__main__":
    main()
