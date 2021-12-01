def luke1silver(filepath):
    with open(filepath) as file:
        lines = file.readlines()
        c = 0
        last = int(lines[0])
        for line in lines[1:]:
            line = int(line)
            if line > last:
                c += 1
                
            last = line
        print(c)

def luke1Gold(filepath):
    with open(filepath) as file:
        lines = [int(e) for e in file.readlines()]
        
        diff = len(lines)%3

        last = sum(lines[0:3])
        c = 0

        for i in range(len(lines)-diff):
            newSum = sum(lines[i:i+3])
            if newSum > last:
                c+=1
            last = newSum
        print(c)

luke1Gold('luke1Gold.txt')