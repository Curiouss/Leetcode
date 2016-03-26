###board= [ [ 0 for i in range(25) ] for j in range(25) ]


def Judge(board,n):
    # board is a 25x25 list
    # player is a int 1 or 2
    # n is a 1x2 list [x,y]
    [x,y]=n
    board[x][y]=1 #define this point to 1 to run the function
    counter = 0
    Judg = [ 0 for i in range(4) ]
    EightArray = [[1,1],[-1,-1],[1,0],[-1,0],[-1,1],[1,-1],[0,1],[0,-1]]
    for Arraynumber in EightArray:
        [xA,xB]= Arraynumber
        print([xA,xB])
        num=1  # connected numbers
        Check = 1
        while Check==True:
            if board[x][y]==board[x+xA*num][x+xB*num]:
                num = num + 1
            else:
            num = num -1
            Check = False
        counter = counter + 0.5
        Judg[int(counter//1)]=Judg[int(counter//1)]+num
    return set(Judg) & {4} == {4}



