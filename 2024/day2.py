from typing import List

def isAllStrictlyIncreasing(l: List[int]) -> bool:
    for i in range(1, len(l)):
        if  l[i] < l[i-1]:
            return False
    return True

def isAllStrictlyDecreasing(l: List[int]) -> bool:
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            return False
    return True


def atMostThreeApart(a: int, b: int) -> bool:
    return abs(a - b) <= 3 and a != b

def checkAdjacent(l: List[int]) -> bool:
    for i in range(1, len(l)):
        if not atMostThreeApart(l[i], l[i-1]):
            return False
    return True

def readFile() -> List[List[int]]:
    with open("2024/day2.txt") as f:
        data = f.read().splitlines()
    return [list(map(int, x.split())) for x in data]

def is_approved(numbers: List[int]) -> bool:
    return checkAdjacent(numbers) and (isAllStrictlyIncreasing(numbers) or isAllStrictlyDecreasing(numbers))

if __name__ == "__main__":
    data = readFile()
    count = 0
    for l in data:
        if is_approved(l):
            count += 1
        else: 
            for i in range(len(l)):
                # Create a new list without the i-th element
                modified_list = l[:i] + l[i+1:]
                if is_approved(modified_list):
                    count += 1
                    break
    print(count)