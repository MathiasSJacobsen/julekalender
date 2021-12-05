
    
def makeMap():
    map = []
    for _ in range(10):
        x = []
        for _ in range(10):
            x.append(0)
        map.append(x)
    return map

def filterLines(lines):
    temp = []
    for e in lines:
        x1 = e[0].strip()[0]
        x2 = e[1].strip()[0]
        y1 = e[0].strip()[2]
        y2 = e[1].strip()[2]
        if x1 == x2 or y1 == y2:
            t1 = [(x1, y1), (x2, y2)]
            temp.append(t1)
    return temp


if __name__ == '__main__':
    lines = [e.split("->") for e in open('test.txt').readlines()]
    
    filterdLines = filterLines(lines)
    map = makeMap()

    for e in filterdLines:
        x1 = int(e[0][0])
        x2 = int(e[1][0])
        y1 = int(e[0][1])
        y2 = int(e[1][1])
        #if x1 < x2:
            #print(x1, y1, x2, y2)
        while x1 <= x2:
            map[y1][x1] = map[y1][x1] + 1
            x1 += 1
            continue
        while x1 >= x2:
            map[y1][x1] = map[y1][x1] + 1
            x1 -= 1
            continue
        while y1 <= y2:
            map[y1][x1] = map[y1][x1] + 1
            y1 += 1
            continue

    print(filterdLines)
    for e in map:
        print(e)