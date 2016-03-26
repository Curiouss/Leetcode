board= [ [ 0 for i in range(25) ] for j in range(25) ]
board[9][9]=1
board[8][8]=1
board[7][7]=1
board[11][11]=1

def Judge(board,n):
    # board is a 25x25 list
    # player is a int 1 or 2
    # n is a 1x2 list [x,y]
    [x,y]=n
##    print(x,y)
    board[x][y]=1 #define this point to 1 to run the function
    counter = -0.5
    Judg = [ 0 for i in range(4) ]
    EightArray = [[1,1],[-1,-1],[1,0],[-1,0],[-1,1],[1,-1],[0,1],[0,-1]]
    for Arraynumber in EightArray:
        [xA,xB]= Arraynumber
        num=1  # connected numbers
        Check = 1
        while Check==True:
##            print([x+xA*num],[y+xB*num])
            if board[x][y]==board[x+xA*num][y+xB*num]:
##                print(num)
                if num >4:
                    Check = False
                num = num + 1
            else:
                num = num -1
                Check = False
        counter = counter + 0.5
##        print(counter,num)
        Judg[int(counter//1)]=Judg[int(counter//1)]+num
##        print(set(Judg))
    return set(Judg) & {4} == {4}



