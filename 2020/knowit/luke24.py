


def readfile(filename):
    info = ""
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            info += line
        return info



def master():
    times = 0
    stamina = 10
    rute = readfile("julaftenrute.txt")
    for house in rute:
        
        times += 1
        
        if house == "1":
            stamina += 2
        stamina -= 1
        if stamina == 0:
            return times



if __name__ == "__main__":
    print(master())