import statistics

def findMean(array):
    return int(statistics.median(array))

def fuelSpending(meanV, array):
    spending = 0
    for e in array:
        spending += abs(e - meanV)
    return spending

def fuelSpendingNewRate(meanV, array):
    
    bestSpening = 10000000000000
    m = max(array)
    mi = min(array) 
    for i in range(mi, m):
        
        spending = 0
        for e in array:
            n = abs(e - i)
            spending += (n*(n+1)//2)
        if bestSpening > spending:
            bestSpening = spending

    return bestSpening

if __name__ == '__main__':
    file = [int(e) for e in open('luke7.txt').readlines()[0].split(',')]
    print(fuelSpendingNewRate(findMean(file), file))
