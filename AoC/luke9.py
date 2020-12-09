from typing import List

x = 25
def main(l):
    for i in range(x ,len(l)):
        preamble = l[i-x:i] 
        b = check(l[i],preamble) 
        if not b:
            return l[i] 
 
def fetch_data():
    numbers = []
    with open("luke9.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                numbers.append(int(line))
    return numbers

def check(checksum, l):
    b = False
    for e in range(len(l)):
        for i in range(1, len(l)):
            #print(l[e] , l[i], l[e] + l[i])
            if (l[e] + l[i]) == checksum:
                b = True
        if b:
            break
    if b:
        return b
    else:
        return b

def contiguous_set(n:int, l:List[int]) -> int:
    count = 0
    s = []
    for i in range(len(l)):
        for e in range(i+1,len(l)):
            count += l[e]
            s.append(l[e])
            if count > n:
                count=0
                s = []
                break
            if count == n:
                m = min(s)
                h = max(s)
                print(s, count, n)
                return m + h


if __name__ == "__main__":
    f = fetch_data()
    num = main(f)
    
    print(contiguous_set(num, f))