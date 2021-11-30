import numpy 
from typing import List # type: ignore

def isPrime(num:int)-> bool:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            else:
                return True
        return False
    
    else:
        return False

def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

def find_nearest(array : List[int], value:int) -> int:
    #array = np.asarray(array)
    idx = (numpy.abs(array - value)).argmin()
    return array[idx]

def findPrime(start:int, end:int)->int:
    temp = []
    for i in range(start+1, int(end*1.5)):
        if i>1:
            for j in range(2,i):
                if(i % j==0):
                    break
            else:
                temp.append(i)
    return temp

def madman(n:int)->int:
    count = 0
    skip = 0
    prime = primesfrom3to(5433000)
    i=0
    while i < n:
        i = str(i)
        if "7" in i:
            i = int(i)
            skip = find_nearest(prime, i)
            i+=skip + 1
            continue
        count += 1
        i = int(i)+ 1
    return count
print(madman(5433000))