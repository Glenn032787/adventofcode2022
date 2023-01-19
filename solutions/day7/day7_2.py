def findPreviousDir(dir_structure, curr):
    for directory in dir_structure:
        if curr in dir_structure[directory]:
            return directory

def addStorage(dir_size, dir_structure, size, curr_dir):
    if curr_dir not in dir_size:
        dir_size[curr_dir] = size
    else:
        dir_size[curr_dir] += size
    
    if curr_dir == "//":
        return dir_size
    previousDir = findPreviousDir(dir_structure, curr_dir)
    dir_size = addStorage(dir_size, dir_structure, size, previousDir)
    return dir_size


def main():
    curr = ''
    dir_structure = {}
    dir_size = {}

    filename = "input.txt"
    #filename = "test.txt"
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if line[0] == "$": # cd command (will pass if ls)
                if line == "$ cd ..":
                   curr = findPreviousDir(dir_structure, curr) 
                elif line[2:4] == "cd":
                    curr = curr + line[5:] + "/"
                elif line == "$ ls":
                    pass
            else: # ls output
                if line[:3] == "dir":
                    new_dir = curr + line[4:] + "/"
                    if curr not in dir_structure:
                        dir_structure[curr] = [new_dir]
                    else:
                        dir_structure[curr].append(new_dir)
                else:
                    size, _ = line.split(' ')
                    size = int(size)
                    dir_size = addStorage(dir_size, dir_structure, size, curr)
    
    unusedSpace = 70000000 - dir_size["//"] 
    spaceToDelete = 30000000 - unusedSpace
    result = []
    for directory in dir_size:
        if dir_size[directory] > spaceToDelete:
            result.append(dir_size[directory])
    print(min(result))


if __name__ == "__main__":
    main()



        
