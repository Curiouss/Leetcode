class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num = nums
        t = target
        L = len(num)
        i = 0
        while i < L:
            if num[i] == t:
                return i
            elif num[i] < t:
                i += 1
            else:
                return i
        return i
