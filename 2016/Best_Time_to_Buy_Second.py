class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        L =len(prices)
        if L == 1:
            return 0
        Lp = prices[0]
        Hp = prices[0]
        Hpr = 0
        for i in range(1,L):
            Hpr =Hpr + max(0,prices[i]-prices[i-1])
        return Hpr
