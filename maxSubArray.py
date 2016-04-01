class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        dp = [0] * size
        ans = -2147483648
        for i in range(0, size):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            ans = max(ans, dp[i])
        return ans
