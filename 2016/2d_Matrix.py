class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        i=0
        j=len(matrix[0])-1
        while i<len(matrix) and j>=0:
            x = matrix[i][j]
            if(target == x):
                return True
            elif(target < x):
                j-=1
            else:
                i+=1
        return False

