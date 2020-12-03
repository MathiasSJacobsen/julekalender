entries = []
with open("luke1.txt") as f:
    for line in f.readlines():
        entries.append(line.strip())
''' part 1
for e in entries:
    for i in entries[1:]:
        if (int(e) + int(i)) == 2020:
            print(e, i)
            print(int(e)*int(i))
'''
for e in entries:
    for i in entries[1:]:
        for l in entries[2:]:
            if (int(e) + int(i) + int(l)) == 2020:
                print(e, i)
                print(int(e)*int(i)*int(l))