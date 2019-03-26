class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s =="" or set(s) == {' '}:
            return 0
        else:
            l = s.split(" ")
            while l[-1] == '':
                l = l[:-1]
            return len(l[-1])
        
        size = len(nums)
        if size == 0:
            return 0
        dp = [0] * size
        ans = -2147483648
        for i in range(0, size):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            ans = max(ans, dp[i])
        return ans
