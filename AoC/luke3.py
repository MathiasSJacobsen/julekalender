
grid = []

with open("luke3.txt") as f:
    for line in f.readlines():
        line = line.strip()
        temp=[]

        for e in line:
            temp.append(e)
        grid.append(temp)



def pritcharPrint(grid):
    for line in grid:
        print(line)

def main():
    rad = 0
    char = 0
    c = 0
    for depth in range(len(grid)-1):
        rad += 1
        char += 3
        char = char % len(grid[0])
        
        if grid[rad][char] == "#":
            c+=1
    run1 = t(1,1)
    run3= t(1, 5)
    run4= t(1, 7)
    run5= t(2, 1)
    print(run1*c*run3*run4*run5)


def t(r, cr):
    rad = 0
    char = 0
    c = 0
    for depth in range(len(grid)-1):
        rad += r
        char += cr

        char = char % len(grid[0])

        if rad > len(grid):
            break
        if grid[rad][char] == "#":
            c+=1

    return c
main()