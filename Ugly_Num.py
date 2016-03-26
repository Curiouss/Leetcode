def isUgly(self, num):
    """
    :type num: int
    :rtype: bool
    """
    N = True
    while N == True:
        if num/2 == num//2:
            num = num//2
        else:
            N = False
    while N == False:
        if num/3 == num//3:
            num = num//3
        else:
            N = True
    while N == True:
        if num/5 == num//5:
            num = num//5
        else:
            N = False
    return num == 1
