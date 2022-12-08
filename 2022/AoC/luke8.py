def readFile():
    with open("2022/AoC/luke8.txt", "r") as f:
        lines = [list(e) for e in f.read().splitlines()]
        for e in lines:
            for i in range(len(e)):
                e[i] = int(e[i])
        return lines

def print2DGrid(grid):
    for row in grid:
        print(row)

def checkIfVisible(grid, x, y):
    checkNumber = grid[y][x]
    currentHi = 0
    isVisible = True

    # Check up
    for _y in range(y):
        if grid[_y][x] > currentHi:
            currentHi = grid[_y][x]
        if currentHi >= checkNumber:
            isVisible = False
    if isVisible: return isVisible
    
    # Check down
    currentHi = 0
    isVisible = True
    for _y in range(y+1, len(grid)):
        if grid[_y][x] > currentHi:
            currentHi = grid[_y][x]
        if currentHi >= checkNumber:
            isVisible = False
    if isVisible: return isVisible
    
    # Check left
    currentHi = 0
    isVisible = True
    for _x in range(x):
        if grid[y][_x] > currentHi:
            currentHi = grid[y][_x]
        if currentHi >= checkNumber:
            isVisible = False
    if isVisible: return isVisible
    
    # Check right
    currentHi = 0
    isVisible = True
    for _x in range(x+1, len(grid[y])):
        if grid[y][_x] > currentHi:
            currentHi = grid[y][_x]
        if currentHi >= checkNumber:
            isVisible = False
    if isVisible: return isVisible
    return isVisible

def ScenicScore(grid, x, y):
    checkNumber = grid[y][x]

    # Check up
    sientificScoreUp = 0
    _y = y - 1
    while _y >= 0:
        if grid[_y][x] >= checkNumber:
            sientificScoreUp += 1
            break
        sientificScoreUp += 1
        _y -= 1
    
    # Check down
    sientificScoreDown = 0
    for _y in range(y+1, len(grid)):
        if grid[_y][x] >= checkNumber:
            sientificScoreDown += 1
            break
        sientificScoreDown += 1
    
    # Check left
    sientificScoreLeft = 0
    _x = x - 1
    while _x >= 0:
        if grid[y][_x] >= checkNumber:
            sientificScoreLeft += 1
            break
        sientificScoreLeft += 1
        _x -= 1
    
    # Check right
    sientificScoreRight = 0
    for _x in range(x+1, len(grid[y])):
        if grid[y][_x] >= checkNumber:
            sientificScoreRight += 1
            break
        sientificScoreRight += 1
    return sientificScoreUp * sientificScoreDown * sientificScoreLeft * sientificScoreRight

def findVisible(grid):
    visible = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if checkIfVisible(grid, x, y):
                visible += 1
    return visible

def findHighestScenicScore(grid):
    highestScore = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            currentScore = ScenicScore(grid, x, y)
            if currentScore > highestScore:
                highestScore = currentScore
    return highestScore

if __name__ == "__main__":
    grid = readFile()
    
    print('Task one:', findVisible(grid))
    print('Task two:', findHighestScenicScore(grid))