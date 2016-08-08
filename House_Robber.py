    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        take = 0
        ntake= 0
        Max = 0
        i = len(nums)
        for x in range(i):
            take = ntake + nums[x]
            ntake = Max
            Max = max(take,ntake)
        return Max