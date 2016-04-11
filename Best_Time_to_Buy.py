class Solution(object):
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        L =len(prices)
        Lp = prices[0]
        Hp = prices[0]
        Cpr = Hp - Lp
        Hpr = Cpr
        for i in range(L):
            if Lp == min(Lp,prices[i]):
                Hp = max(Hp, prices[i])
                Cpr = Hp-Lp
            else:
                Lp = prices[i]
                Hp = Lp
            Hpr =max(Cpr,Hpr)
        return Hpr
