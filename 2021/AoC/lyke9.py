def heightMap(array):
    lowPoints = []
    for i in range(1, len(array)-1):
        for j in range(1, len(array[i])-1):
            currentPoint = array[i][j]
            if array[i-1][j] > currentPoint and array[i + 1][j] > currentPoint and array[i][j-1] > currentPoint and array[i][j+1] > currentPoint:
                lowPoints.append(currentPoint)
    return lowPoints

def calculateRiskLevel(array):
    return sum([int(a) + 1 for a in array])
if __name__ == '__main__':
    file = ['9' + e.strip() + '9' for e in open('luke9.txt').readlines()]
    file.insert(0, '9' * len(file[0]))
    file.append('9' * len(file[0]))
    print(calculateRiskLevel(heightMap(file)))
