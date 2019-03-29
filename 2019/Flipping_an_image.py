class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B=[]
        for li in A:
            B.append(li[::-1])
        for x in range(len(B)):
            for y in range(len(B[0])):
                if B[x][y]==1:
                    B[x][y]=0
                else:
                    B[x][y]=1
        return B
