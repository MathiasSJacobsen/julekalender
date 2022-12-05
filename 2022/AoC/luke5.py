import copy
crates = [
    ['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'],
    ['N', 'B', 'L'],
    ['J', 'C', 'H', 'T', 'L', 'V'],
    ['S', 'P', 'J', 'W'],
    ['Z', 'S', 'C', 'F', 'T', 'L', 'R'],
    ['W', 'D', 'G', 'B', 'H', 'N', 'Z'],
    ['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'],
    ['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'],
    ['R', 'P', 'M', 'L', 'H']
]

def readFile(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()[10:]]
                
def findCoords(lst):
    coords = []
    for e in lst:
        line = e.split()
        n, _from, _to = line[1], line[3], line[-1]
        coords.append((n, _from, _to))
    return coords

def moveCratesTaskOne(coords):
    myCreates = copy.deepcopy(crates)
    for n, _from, _to in coords:
        for _ in range(int(n)):
            crate = myCreates[int(_from)-1].pop()
            myCreates[int(_to)-1].append(crate)
    return myCreates

def moveCratesTaskTwo(coords):
    myCreates = copy.deepcopy(crates)
    for n, _from, _to in coords:
        _crates = myCreates[int(_from)-1][-int(n):]
        myCreates[int(_from)-1] = myCreates[int(_from)-1][:-int(n)]
        myCreates[int(_to)-1].extend(_crates)
    return findSolution(myCreates)


def findSolution(_crates):

    return ''.join([e[-1] for e in _crates])

if __name__ == '__main__':
    print('Task one:', findSolution(moveCratesTaskOne(findCoords(readFile('2022/AoC/luke5.txt')))))
    print('Task two:', findSolution(moveCratesTaskTwo(findCoords(readFile('2022/AoC/luke5.txt')))))