def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    # Create a list for the loop.
    
    def f(x):
        return x*x
    import re

    def Luc(num):
        m = re.findall('[0-9]',str(num))
        l = ','.join(m)
        n = 0
        s =""
        while n < len(l):
            s += str(l[n])
            n += 1
        s = re.sub(" ", "", s)
        s = [int(i) for i in s.split(',')]
       #s = re.sub(" ", "", s)
        s = map(f,s)
        s = sum(list(s))
        return s

    Num = set(str(n))
    Q = 1
    LuckY = {'1'}
    while Q == True:
        if str(Luc(n)) in LuckY:
            return True
        else:
            if str(Luc(n)) in Num:
                return False
            else:
                n = Luc(n)
                Num.add(str(n))
