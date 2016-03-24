
n = 5
N = bin(n)
N = str(N)
L = len(N)-1
count = 0
def Weight(L):
    if L == 1:
        return count
    elif L == 0:
        return 0

    else:
        if N[L]=='1':
            return 1 + Weight(L-1)
        else:
            return Weight(L-1)

Weight(L)
