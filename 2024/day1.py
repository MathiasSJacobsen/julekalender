from collections import Counter

def distance(list1, list2):
    list1.sort()
    list2.sort()
    return sum([abs(list1[i] - list2[i]) for i in range(len(list1))])

def read_file(filename):
    list1 = []
    list2 = []
    with open(filename) as f:
        for line in f.readlines():
            [number1, number2]= line.strip().split("   ")
            list1.append(int(number1))
            list2.append(int(number2))
    return list1, list2

def similarity_score(leftSide, rightSide):
    counterRight = Counter(rightSide)
    return sum([i*counterRight[i] for i in leftSide])


if __name__ == '__main__':
    [lst1, lst2]=read_file('2024/day1.txt')
    print("Silver star:", distance(lst1, lst2))
    print("Gold star:", similarity_score(lst1, lst2))