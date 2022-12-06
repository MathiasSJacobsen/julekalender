def readFile(filename):
    with open(filename) as f:
        return f.readline()

def findFirstFourUniqueCharsInARow(string):
    for i in range(len(string)-3):
        unique = set(string[i:i+4])
        if len(unique) == 4:
            return i + 4
    return None

def findFirstFourteenUniqueCharsInARow(string):
    for i in range(len(string)-13):
        unique = set(string[i:i+14])
        if len(unique) == 14:
            return i + 14
    return None

if __name__ == "__main__":
    string = readFile("2022/AoC/luke6.txt")
    print('Task 1:', findFirstFourUniqueCharsInARow(string))
    print('Task 2:', findFirstFourteenUniqueCharsInARow(string))