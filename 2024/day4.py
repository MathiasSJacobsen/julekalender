def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    length = len(word)

    directions = [
        (-1,  0), 
        ( 1,  0), 
        ( 0, -1), 
        ( 0,  1), 
        (-1, -1), 
        (-1,  1), 
        ( 1, -1), 
        ( 1,  1)  
    ]

    total_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 'X':
                continue

            for dr, dc in directions:
                found = True
                rr, cc = r, c  
                for i in range(length):
                    if not (0 <= rr < rows and 0 <= cc < cols):
                        found = False
                        break

                    if grid[rr][cc] != word[i]:
                        found = False
                        break
                    rr += dr
                    cc += dc

                if found:
                    total_count += 1

    return total_count

def count_x_mas_2(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def diagonal_ok(a, b):
        return (a == 'M' and b == 'S') or (a == 'S' and b == 'M')

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == 'A':

                tl = grid[r-1][c-1]
                br = grid[r+1][c+1]

                tr = grid[r-1][c+1]
                bl = grid[r+1][c-1]

                if diagonal_ok(tl, br) and diagonal_ok(tr, bl):
                    count += 1

    return count

def readFile():
    with open("2024/day4.txt") as f:
        data = f.read().splitlines()
    return data

if __name__ == "__main__":
    grid = readFile()

    result = count_xmas(grid)
    result2 = count_x_mas_2(grid)
    print("Number of 'XMAS' occurrences:", result)
    print("Number of 'X-MAS' occurrences:", result2)
