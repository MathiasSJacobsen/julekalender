def silver(filename):
    with open(filename) as f:
        mx = -1
        s = 0
        for line in f.readlines():
            if line == '\n':
                mx = max(mx, s)
                s = 0
            else: s += int(line)
        mx = max(mx, s)
        return mx

def gold(filename):
    with open(filename) as f:
        l = []
        s = 0
        for line in f.readlines():
            if line == '\n':
                l.append(s)
                s = 0
            else: s += int(line)
        l.append(s)
        l.sort()
        return sum(l[-3:])

if __name__ == '__main__':
    print(silver('luke1.txt'))
    print(gold('luke1.txt'))