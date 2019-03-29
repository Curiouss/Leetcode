class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total=sum(A)
        # if total//3 !=total/3.0:
        #     return False
        eq=total//3
        if len(A)<3:
            return False
        i=0
        j=len(A)-1
        s1=""
        s3=""
        while i<len(A)-2:
            if not s1:
                s1=0
            s1+=A[i]
            if s1==eq:
                break
            i+=1
        while j>1:
            if not s3:
                s3=0
            s3+=A[j]
            if s3==eq:
                break
            j-=1
        print i,j,len(A)
        if j==1 or i==len(A)-2 or j-i<2:
            return False
        else:
            return True
        
            
