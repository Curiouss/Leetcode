class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return set(bin(n)[3:])=={'0'} or n==1
