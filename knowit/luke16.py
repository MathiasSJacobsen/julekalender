import string

def master(filename):
    letters = string.ascii_lowercase
    with open(filename, "r") as f:
        line = list(f.readline())
        print("".join(line))

        line = re(line, "x")

        print("".join(line))
        

def re(l, a):
    letter_index = list(string.ascii_lowercase).index(a)

    c = 0
    idx = 0
    for e in l:
        if e == a and c != letter_index:
            l.pop(idx)
            c+=1
        elif e == a:
            c+=1
        idx+=1
        
    return l


if __name__ == "__main__":
    master("test.txt")