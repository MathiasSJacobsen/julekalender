l=[]
with open("numbers.txt") as f:
    for line in f.readlines():
        l=line.split(",")
e=[int(x) for x in l]
e.sort()
for i in range(len(e)-1):
    if (e[i] + 1) != e[i+1]:
        print(e[i])