class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s =="" or set(s) == {' '}:
            return 0
        else:
            l = s.split(" ")
            while l[-1] == '':
                l = l[:-1]
            return len(l[-1])
        
