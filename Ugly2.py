def nthUglyNumber(self, n):
    def isUgly(num):
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num /= x
        return num == 1
    i=0
    Num=0
    while i<n:
        Num+=1
        if isUgly(Num):
            i+=1
    return Num


class Solution:
    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n):
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < n:
            m2, m3, m5 = q[i2] * 2, q[i3] * 3, q[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            q += m,
        return q[-1]
