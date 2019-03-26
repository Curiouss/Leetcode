# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
##
##class Solution(object):
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    Ver == True
    array = lsit(range(1,n))
    low = 0
    height = len(array)-1
    while low < height:
        mid = (low+height)/2
        if isBadVersion(array[mid]) != 0:
            low = mid + 1

        elif isBadVersion(array[mid]) != 1:
            height = mid - 1

        else:
            return array[mid]

            
