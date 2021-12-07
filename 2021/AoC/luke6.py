from typing import List, Dict


def sim(array:List[int]):
    array.sort()
    for _ in range(256):
        array = step(array)
        if(_ % 10 == 0):
            print(_)
    print(len(array))


def step(array):
    tarray = []
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = 7
            tarray.append(8)
        tarray.append(array[i] - 1)
    return tarray


def sim1(array:List[int]):
    d = {}
    for e in array:
        d.setdefault(e, 0)
        d[e] = d[e]+ 1
    for _ in range(256):
        d = step1(d)
    print(sum(d.values()))

    
def step1(dct:Dict):
    newD = {}
    for k, v in dct.items():

        if k == 0:
            newD.setdefault(6, 0)
            newD[6] = newD[6] + v
            newD.setdefault(8, 0)
            newD[8] = newD[8] + v 
        else:
            newD.setdefault(k-1, 0)
            newD[k-1] = newD[k-1] + v
    return newD
        




if __name__ == '__main__':
    file = [int(e) for e in open('luke6silver.txt').readline() if e != ',' ]
    #sim(file)
    sim1(file)