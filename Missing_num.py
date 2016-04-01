def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    L = len(nums)
    S = set(range(L + 1))
    N = set(nums)
    NUM = S - N
    t = list(NUM)
    return t[0]
