def readFile():
    with open("2022/AoC/luke10.txt", "r") as f:
        return f.read().splitlines()

def run():
    cycle = 0
    x = 1
    result = []
    lines = readFile()
    printedLines = []
    for line in lines:
        splited = line.split(" ")
        if splited[0] == "noop":
            cycle = noop(cycle, x, result, printedLines)
        elif splited[0] == "addx":
            cycle, x = addx(cycle, x, int(splited[1]), result, printedLines)

    return sum(result)
    
        

def check(cycle, x, result):
    if cycle in [20, 60, 100, 140, 180, 220]:
       # print((x * cycle))
        result.append(x * cycle)

def CRT(line, x, cycle):
    _cycle = cycle % 40
    if _cycle in [x-1, x, x+1]:
        #line.append("#")
        print("#", end="")
    else:
        #line.append(".")
        print(".", end="")
    if (cycle+1) % 40 == 0 and cycle != 0:
        print()
        #line.append("\n")
    


def noop(cycle, x, result, printedLines):
    CRT(printedLines, x, cycle)
    cycle += 1
    check(cycle, x, result)
    return cycle

def addx(cycle, x, addX, result, printedLines):
    for _ in range(2):
        CRT(printedLines, x, cycle)
        cycle += 1
        check(cycle, x, result)
    return cycle, x + addX

if __name__ == "__main__":
    run()