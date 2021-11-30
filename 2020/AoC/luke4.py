# Part 1
def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        temp = {}
        c = 0
        for line in f.readlines():
            line = line.strip()

            if not line == "":
                line = line.split()
                for e in line:
                    e = e.split(":")
                    temp.setdefault(e[0], e[1])
            else:
                b = check(temp)
                if b:
                    c+=1
                temp={}
        # gjør funksjoen her også
        b = check(temp)
        if b:
            c+=1
        print(c)

def check(d):
    t = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # "cid" not importes
    for e in d.keys():
        if e in t:
            t.remove(e)
    if len(t) == 0:
        return True
    return False

# Part 2
def master():
    with open("input.txt", "r", encoding="utf-8") as f:
        temp = {}
        c = 0
        t = 0
        for line in f.readlines():
            line = line.strip()

            if not line == "":
                line = line.split()
                for e in line:
                    e = e.split(":")
                    temp.setdefault(e[0], e[1])
            else:
                if (check(temp)):
                    b = checks(temp)
                    if b:
                        c+=1
                temp={}
                
                
                
        # gjør funksjoen her også
        if (check(temp)):

            b = checks(temp)
            if b:
                c+=1
        print(c)

def checks(d):
    ecl_values = "amb blu brn gry grn hzl oth".split(" ")
    hcl_values = "0 1 2 3 4 5 6 7 8 9 a b c d e f".split(" ")


    byr = d["byr"]
    iyr = d["iyr"]
    eyr = d["eyr"]
    hgt = d["hgt"][:-2]

    value = d["hgt"][-2:]
    hcl = d["hcl"]
    ecl = d["ecl"]
    pid = d["pid"]


    #print(byr, iyr, eyr, hgt, value, hcl, ecl, pid)
    if int(byr) < 1920 or int(byr) > 2002:
        return False
    if int(iyr) < 2010 or int(iyr) > 2020:
        return False
    if int(eyr) < 2020 or int(eyr) > 2030:
        return False
    if value == "cm":
        if int(hgt) < 150 or int(hgt) > 193:
            return False
    elif value == "in":
        if int(hgt) < 59 or int(hgt) > 76:
            return False
    else:
        print(d)
        return False
    if not len(hcl[1:]) == 6 or not hcl[0] == '#':
        return False
    for e in hcl[1:]:
        if not e in hcl_values:
            return False
    if not ecl in ecl_values:
        return False
    if not len(pid) == 9 or not pid.isdigit():
        return False
    return True


if __name__ == "__main__":
    #main()
    master()