##
##import math
##
##
##def producePrime2(max):
##    counter = 0
##    li = []
##    for i in range(2, max + 1):
##        if i > 2 and i % 2 == 0:
##            li.append(0)
##        else:
##            li.append(i)
##
##    for i in range(3, int(math.sqrt(max)) + 1, 2):
##        if li[i - 2] != 0:
##            for j in range(i + i, max + 1, i):
##                li[j - 2] = 0
##
##    for i in li:
##        if i != 0:
##            counter += 1
##
##    return counter
##
##
##producePrime2(10)
def countPrimes(self, n):
    isPrime = [True] * max(n, 2)
    isPrime[0], isPrime[1] = False, False
    x = 2
    while x * x < n:
        if isPrime[x]:
            p = x * x
            while p < n:
                isPrime[p] = False
                p += x
        x += 1
    return sum(isPrime)
