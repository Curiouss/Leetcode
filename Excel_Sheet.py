#code for 168
def convertToTitle(self, n):
    rest = n
    Excel=''
    Count=0
    while rest>26:
        rest=rest//26
        Count+=1
    for i in range(Count,-1,-1):
        Num=n//(26**i)
        Char=chr(Num+64)
        n=n-Num*(26**i)
        Excel=Excel+Char
    return(Excel)