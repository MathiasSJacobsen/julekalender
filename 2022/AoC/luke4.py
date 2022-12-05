def mainPartOne(filepath):
    s = 0
    with open(filepath) as f:
        lines = f.readlines()
        for e in lines:
            sectorOne, sectorTwo = e.strip().split(',')
            x1, x2 = sectorOne.split('-')
            y1, y2 = sectorTwo.split('-')
            s += 1 if overlap(int(x1), int(x2), int(y1), int(y2)) else 0
    return s


def overlap(x1, x2, y1, y2):
    x = range(x1, x2+1)
    y = range(y1, y2+1)
    intersection = set(x).intersection(y)
    return True if len(intersection) > 0 else False

def fullyOverlap(x1, x2, y1, y2):
    return x1 >= y1 and x2 <= y2 or y1 >= x1 and y2 <= x2

def mainPartTwo(filepath):
    s = 0
    with open(filepath) as f:
        lines = f.readlines()
        for e in lines:
            sectorOne, sectorTwo = e.strip().split(',')
            x1, x2 = sectorOne.split('-')
            y1, y2 = sectorTwo.split('-')
            s += 1 if overlap(int(x1), int(x2), int(y1), int(y2)) else 0
    return s

if __name__ == '__main__':
    print(mainPartOne('2022/AoC/test.txt'))
    print(mainPartTwo('2022/AoC/luke4.txt'))