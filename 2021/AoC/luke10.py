from typing import List


def calculatepoints(list: List[str]) -> int:
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    p = 0
    for bracket in list:
        p += points[bracket]

    return p


def filterCorruptedFiles(list: List[str]) -> List[str]:

    brackets = {
        '>': '<',
        ')': '(',
        ']': '[',
        '}': '{',
    }
    incorrect = []
    scoresForFixing = []

    for line in list:
        t = True
        stack = []
        for char in line:
            if char in brackets.values():
                stack.append(char)
            else:  # char in brackets.keys()
                item = stack.pop()
                if item != brackets[char]:
                    incorrect.append(char)
                    t = False
                    break
        if t:
            scoresForFixing.append(calculatePoiontsForFixingLines(stack))
    scoresForFixing.sort()
    print(scoresForFixing[len(scoresForFixing)//2])
    return incorrect

def calculatePoiontsForFixingLines(list : List[str]):
    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    p = 0
    for char in list[::-1]:
        p = p * 5 + points[char]
    return p

if __name__ == '__main__':
    
    file = [e.strip() for e in open('luke10.txt').readlines()]
    print(calculatepoints(filterCorruptedFiles(file)))
