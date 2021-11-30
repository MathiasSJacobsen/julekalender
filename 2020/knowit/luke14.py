
winners = {}


def main(filename):
    with open(filename, "r") as f:
        for l in f.readlines():
            line = ""
            for e in l:
                if e != ",": # Had to remove , for the winner thing
                    line += e

            numbers = line[:4].split()
            rule = int(numbers[0])
            steps = int(numbers[1])
            if steps > 9:
                alves = line.strip()[6:-1].split() # Removes the [ ]
            else:
                alves = line.strip()[5:-1].split() # Removes the [ ]
            current = 0

            while len(alves) > 1:
                if current > len(alves)-1:
                    current = 0 
                temp = list(alves)
                alves = exchange(steps, temp)

                alves = out(rule, current, len(alves), alves)
                current += 1
                
            winners[alves[0]] = winners.setdefault(alves[0], 0) + 1

    max_key = max(winners, key=winners.get)

    print(winners[max_key])
    print(max_key)
            

def exchange(n, l):
    out = [x for x in range(len(l))]
    
    for i in range(len(l)):
        alv = l[i]
        out[(i+n)%len(l)] = alv
    return out

def out(n, current, lenght, l):

    if n == 1:
        l.pop(0)

    elif n == 2:
        l.pop(current)
        
    elif n == 3:
        if lenght == 2:
            l.pop(0)
        elif lenght % 2 == 0:
            l.pop(lenght // 2)
            l.pop((lenght // 2) - 1)
        else:
            l.pop(lenght // 2)
        
    else:
        l.pop(-1)

    return l


if __name__ == "__main__":
    main("luke14.txt")