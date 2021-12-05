
    
def makeMap():
    map = []
    for _ in range(1000):
        x = []
        for _ in range(1000):
            x.append(0)
        map.append(x)
    return map

def filterLines(lines):
    temp = []
    for e in lines:
        
        x1 = e[0].strip().split(',')[0]
        x2 = e[1].strip().split(',')[0]
        y1 = e[0].strip().split(',')[1]
        y2 = e[1].strip().split(',')[1]
        if x1 == x2 or y1 == y2:
            t1 = [(x1, y1), (x2, y2)]
            temp.append(t1)
    return temp


if __name__ == '__main__':
    lines = [e.split("->") for e in open('luke5silver.txt').readlines()]
    
    filterdLines = filterLines(lines)
    map = makeMap()

    for e in filterdLines:
        print(e)
        x1 = int(e[0][0])
        x2 = int(e[1][0])
        y1 = int(e[0][1])
        y2 = int(e[1][1])
        #if x1 < x2:
            #print(x1, y1, x2, y2)
        while x1 < x2:
            map[y1][x1] = map[y1][x1] + 1
            x1 += 1
            continue
        while x1 > x2:
            map[y1][x1] = map[y1][x1] + 1
            x1 -= 1
            continue
        while y1 < y2:
            map[y1][x1] = map[y1][x1] + 1
            y1 += 1
            continue
        while y1 >= y2:
            map[y1][x1] = map[y1][x1] + 1
            y1 -= 1
            continue

    s = 0
    for e in map:
        for i in e:
            if i > 1:
                s +=1
    print(s)