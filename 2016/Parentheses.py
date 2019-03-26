def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    n=2*n
    Output=list()
    for i in range(2**(n-1),2**n):
        Count = -1
        Num=bin(i)
        Data=0
        Balance=0
        String=''
        while Data>-1:
            if Num[Count]=='0':
                Data +=1
                Balance +=1
                String=')'+String
            elif Num[Count]=='1':
                Data -=1
                Balance -=1
                String='('+String
            elif Num[Count]=='b':
                if Balance == 0:
                    Output.append(String)
                Data=-1
            Count-=1
    return Output


