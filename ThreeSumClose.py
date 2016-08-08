    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        Length=len(nums)
        Rtarget=-2**32
        for i in range(Length-3):
            for j in range(i,Length-2):
                for k in range(j,Length-1):
                    Sum = nums[i]+nums[j]+nums[k]
                    if abs(Rtarget-target)>abs(Sum-target):
                    Rtarget = Sum
        return Rtarget


 www.ybjk.com