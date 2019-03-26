class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        else:
            Nums = set(nums)
            num_new = list(Nums)
            return len(nums) != len(num_new)
