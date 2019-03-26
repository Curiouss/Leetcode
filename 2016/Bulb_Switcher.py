def bulbSwitch(self, n):
    """
    :type n: int
    :rtype: int
    """
##    count = 2
##    if n == 0:
##        return 0
##    if n == 1:
##        return 1
##    N = set(range(n+1))-set(range(1))
##    while count<=n:
##        C = n//count
##        L =list(range(C+1))
##        N2 = set(i*count for i in L) - set(range(1))
##        N = N.union(N2) - N.intersection(N2)
##        count += 1
##    return len(N)
    import math
    return len(range(0, int(math.sqrt(n))))
