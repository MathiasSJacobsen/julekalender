def points(c):
    d = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        'A': 27,
        'B': 28,    
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52,
    }
    return d[c]

def mainPartOne(filepath):
    with open(filepath) as f:
        s = 0
        for line in f.readlines():
            line = line.strip()
            partOne, partTwo = line[:len(line)//2], line[len(line)//2:]
            char = findChrPartOne(partOne, partTwo)
            s += points(char)
        return s

def findChrPartOne(a, b):
    for e in a:
        if e in b:
            return e

def mainPartTwo(filepath):
    with open(filepath) as f:
        s = 0
        lines = f.readlines()
        for i in range(0, len(lines) - 1, 3):
            line1, line2, line3 = lines[i], lines[i+1], lines[i+2]
            char = findChrPartTwo(line1, line2, line3)
            s += points(char)
        return s

def findChrPartTwo(a, b, c):
    for e in a:
        if e in b and e in c:
            return e

if __name__ == '__main__':
    print('Part one:', mainPartOne('2022/AoC/luke3.txt'))
    print('Part two:', mainPartTwo('2022/AoC/luke3.txt'))
