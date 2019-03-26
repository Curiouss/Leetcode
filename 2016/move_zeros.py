def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    L = len(nums)-1
    i = L
    N = []
    for x in range(L,0,-1):
        if nums[x] == 0:
            if x == L:
                nums = nums[0:x]
            else:
                numsend = nums[x+1:]
                nums = nums[0:x]
                nums= nums +numsend
            N.append(i)
        i = i + 1
    L_zero = len(N)
    nums = nums + [0]*L_zero
    return nums
