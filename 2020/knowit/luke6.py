from collections import Counter

with open("godteri.txt", "r") as f:
    line = f.readline().split(",")
    counter = Counter(line)
    print(counter)
    
