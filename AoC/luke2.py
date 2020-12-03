c = 0
'''
with open("luke2.txt") as f:

    for line in f.readlines():
        line=line.strip()
        parts = line.split(" ")
        occ = parts[0].split("-")
        char = parts[1][0]
        password = parts[2]
        t = 0
        for pwd in password:
            if char == pwd:
                t += 1
        if int(occ[0]) > t or t > int(occ[1]):
            continue
        c+=1
'''

with open("luke2.txt") as f:
    for line in f.readlines():
        line=line.strip()
        parts = line.split(" ")
        occ = parts[0].split("-")
        char = parts[1][0]
        password = parts[2]
        t = 0
        
        if not (password[int(occ[0])-1] == char and password[int(occ[1])-1] == char) and (password[int(occ[0])-1] == char or password[int(occ[1])-1] == char):
            c+=1





print(c)
