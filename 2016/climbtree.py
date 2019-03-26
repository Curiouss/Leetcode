def Excel(s):
    L = len(s)
    i = L
    j = 0
    Num = 0
    print(i)
    while i>0:
        Num = Num + (26**j)*(ord(s[i-1])-64)
        i = i - 1
        j = j + 1
    return Num

print(Excel("A"))
