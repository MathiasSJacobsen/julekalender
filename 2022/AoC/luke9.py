
class Pice:
    def __init__(self):
        self.cooordinates = [(0, 0)]

    def __repr__(self):
        return self.cooordinates

    def __str__(self):
        return self.cooordinates

def readFile():
    with open("2022/AoC/luke9.txt", "r") as f:
        return [e.split(" ") for e in f.read().splitlines()]

def moveHead(pice, dir):
    currentPos = pice.cooordinates[-1]
    if dir == "U":
        pice.cooordinates.append((currentPos[0], currentPos[1] + 1))
    elif dir == "D":
        pice.cooordinates.append((currentPos[0], currentPos[1] - 1))
    elif dir == "R":
        pice.cooordinates.append((currentPos[0] + 1, currentPos[1]))
    elif dir == "L":
        pice.cooordinates.append((currentPos[0] - 1, currentPos[1]))
    
def moveTail(head, tail, dir):
    headCurrentPos = head.cooordinates[-1]
    tailCurrentPos = tail.cooordinates[-1]

    if headCurrentPos in findCoordinatesAround(tailCurrentPos):
        return
    tail.cooordinates.append(head.cooordinates[-2])

def moveTails(before, current, dir):
    beforeCurrentPos = before.cooordinates[-1]
    currentCurrentPos = current.cooordinates[-1]
    if beforeCurrentPos in findCoordinatesAround(currentCurrentPos):
        return
    if beforeCurrentPos[0] > currentCurrentPos[0] and beforeCurrentPos[1] > currentCurrentPos[1]:
        current.cooordinates.append((currentCurrentPos[0] + 1, currentCurrentPos[1] + 1))
    elif beforeCurrentPos[0] > currentCurrentPos[0] and beforeCurrentPos[1] < currentCurrentPos[1]:
        current.cooordinates.append((currentCurrentPos[0] + 1, currentCurrentPos[1] - 1))
    elif beforeCurrentPos[0] < currentCurrentPos[0] and beforeCurrentPos[1] > currentCurrentPos[1]:
        current.cooordinates.append((currentCurrentPos[0] - 1, currentCurrentPos[1] + 1))
    elif beforeCurrentPos[0] < currentCurrentPos[0] and beforeCurrentPos[1] < currentCurrentPos[1]:
        current.cooordinates.append((currentCurrentPos[0] - 1, currentCurrentPos[1] - 1))
    elif beforeCurrentPos[0] > currentCurrentPos[0]:
        current.cooordinates.append((currentCurrentPos[0] + 1, currentCurrentPos[1]))
    elif beforeCurrentPos[0] < currentCurrentPos[0]:
        current.cooordinates.append((currentCurrentPos[0] - 1, currentCurrentPos[1]))
    elif beforeCurrentPos[1] > currentCurrentPos[1]:
        current.cooordinates.append((currentCurrentPos[0], currentCurrentPos[1] + 1))
    elif beforeCurrentPos[1] < currentCurrentPos[1]:
        current.cooordinates.append((currentCurrentPos[0], currentCurrentPos[1] - 1))

def findCoordinatesAround(currentPos):
    return [
        currentPos,
        (currentPos[0] + 1, currentPos[1]),
        (currentPos[0] - 1, currentPos[1]),
        (currentPos[0], currentPos[1] + 1),
        (currentPos[0], currentPos[1] - 1),
        (currentPos[0] - 1, currentPos[1] - 1),
        (currentPos[0] + 1, currentPos[1] + 1),
        (currentPos[0] + 1, currentPos[1] - 1),
        (currentPos[0] - 1, currentPos[1] + 1)
    ]  

def taskOne():
    cmd = readFile()
    head = Pice()
    tail = Pice()
    for _cmd in cmd:
        direction, steps = _cmd[0], int(_cmd[1])
        for _ in range(steps):
            moveHead(head, direction)
            moveTail(head, tail, direction)
    return len(set(tail.cooordinates))

def taskTwo():
    cmd = readFile()
    head = Pice()
    one = Pice()
    two = Pice()
    three = Pice()
    four = Pice()
    five = Pice()
    six = Pice()
    seven = Pice()
    eight = Pice()
    nine = Pice()
    for _cmd in cmd:
        direction, steps = _cmd[0], int(_cmd[1])
        for _ in range(steps):
            moveHead(head, direction)
            moveTails(head, one, direction)
            moveTails(one, two, direction)
            moveTails(two, three, direction)
            moveTails(three, four, direction)
            moveTails(four, five, direction)
            moveTails(five, six, direction)
            moveTails(six, seven, direction)
            moveTails(seven, eight, direction)
            moveTails(eight, nine, direction)
    return len(set(nine.cooordinates))


    
if __name__ == "__main__":
    print('Task one:', taskOne())
    print('Task two:', taskTwo())
