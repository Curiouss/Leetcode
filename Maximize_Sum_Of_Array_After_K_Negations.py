class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        neg=[]
        pos=[]
        for num in A:
            if num<=0:
                neg.append(num)
            else:
                pos.append(num)
        neg=sorted(neg)
        pos=sorted(pos)

        if K>=len(neg) and (K-len(neg))%2==1:
            if len(neg)==0:
                pos[0]=-pos[0]
                return sum(pos)
            else:
                return max((sum(pos)-sum(neg)+2*neg[-1]),((sum(pos)-sum(neg)-2*pos[0])))
        elif K>=len(neg) and (K-len(neg))%2!=1:
            return sum(pos)-sum(neg)
        else:
            for i in range(K):
                neg[i]=-neg[i]
            return sum(pos)+sum(neg)
