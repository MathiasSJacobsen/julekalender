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

    for line in list:
        stack = []
        for char in line:
            if char in brackets.values():
                stack.append(char)
            else:  # char in brackets.keys()
                item = stack.pop()
                if item != brackets[char]:
                    incorrect.append(char)
                    break
    return incorrect

if __name__ == '__main__':
    
    file = [e.strip() for e in open('luke10.txt').readlines()]
    print(calculatepoints(filterCorruptedFiles(file)))
