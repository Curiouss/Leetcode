# The ways for 12121

def numDecodings(s):
    import re
    def f(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        return f(n-1)+f(n-2)
    counter1 = 0
    counter2 = 0
    Combo = False
    Len =len(s)
    if s == "":
        return 0
    if s[0] =="0":
        return 0
    for i in range(len(s)):
        if s[i] =="2" or s[i] == "1":
            counter2 += 1
            if i < Len-1:
                for j in list(range(3,7)):
                    if s[i+1] ==str(j):
                        counter2 += 1
                        Combo = True
                if s[i+1] !="1" and s[i+1] != "2" and Combo == False:
                    Combo = True
            elif i == Len-1:
                Combo = True
                
                    
        for j in range(1,10):
            if s[i] ==str(j) and counter1 ==0:
                counter1 = 1

        while Combo == True:
            if counter2 ==1:
                counter2 -=1
            counter1 = counter1 + f(counter2)-1
            counter2 = 0
            Combo = False
    return(counter1)
