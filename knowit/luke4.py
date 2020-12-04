
d = {}
with open("leveringsliste.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.strip()
        line = line.split(",")
        for e in line:
            temp = e.split()
            
            d[temp[0]] = d.setdefault(temp[0],0) + int(temp[1])
print(d)
sukker = d["sukker:"] // 2
melk = d["melk:"]// 3
egg = d["egg:"]// 1
mel = d["mel:"]// 3
print(min(sukker, melk, egg, mel))