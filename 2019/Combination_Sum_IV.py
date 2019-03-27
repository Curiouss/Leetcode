class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        dp=[0]*(1+target)
        dp[0]=1
        nums=sorted(nums)
        for k in xrange(nums[0],target+1):
            for num in nums:
                if k>=num:
                    dp[k]+=dp[k-num]
        return dp[-1]
