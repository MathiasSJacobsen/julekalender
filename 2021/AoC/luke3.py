def luke1silver(path):
    with open(path) as file:
        lines = file.readlines()
        gamma = ""
        for x in range(len(lines[0])-1):
            en = 0
            null = 0
            for y in range(len(lines)):
                if lines[y][x] == "1":
                    en += 1
                else:
                    null += 1
            if en > null:
                gamma += '1'
            else: 
                gamma += '0'

        print(int(rev(gamma), 2)*int(gamma, 2))
        

def rev(string):
    t =''
    for e in string:
        t += str((int(e) + 1)%2)
    return t


def findMostCommen(x, listOfBits):
    en = 0
    tableWithOnes = []
    null = 0
    tableWithZeros = []
    for y in range(len(listOfBits)):
        if listOfBits[y][x] == "1":
            en += 1
            tableWithOnes.append(listOfBits[y])
        else:
            null += 1
            tableWithZeros.append(listOfBits[y])
    if en >= null:
        return '1', tableWithOnes
    else: 
        return '0', tableWithZeros

def findLeastCommen(x, listOfBits):
    en = 0
    tableWithOnes = []
    null = 0
    tableWithZeros = []
    for y in range(len(listOfBits)):
        if listOfBits[y][x] == "1":
            en += 1
            tableWithOnes.append(listOfBits[y])
        else:
            null += 1
            tableWithZeros.append(listOfBits[y])
    if en >= null:
        return '0', tableWithZeros
    else: 
        return '1', tableWithOnes


def oxygenGeneratorRating(listOfBits, x = 0):
    if len(listOfBits) == 1:
        return listOfBits[0]
    return oxygenGeneratorRating(findMostCommen(x, listOfBits)[1], x+1)

def CO2ScrubberRating(listOfBits, x = 0):
    if len(listOfBits) == 1:
        return listOfBits[0]
    return CO2ScrubberRating(findLeastCommen(x, listOfBits)[1], x+1)

if "__main__" == __name__:
    # luke1silver('luke3silver.txt')
    with open("luke3silver.txt") as file:
        lines = [e.strip() for e in file.readlines()]
        print(int(oxygenGeneratorRating(lines), 2))
        print(int(CO2ScrubberRating(lines), 2))
        print(int(oxygenGeneratorRating(lines), 2) * int(CO2ScrubberRating(lines), 2))