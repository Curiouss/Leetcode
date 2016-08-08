class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        Len = len(digits)
        Num = 1
        for x in range(Len):
            Num = Num + digits[x]*(10**(Len-x-1))
        Newlist=str(Num)
        N=[]
        for x in Newlist:
            N.extend([int(x)])
        return N