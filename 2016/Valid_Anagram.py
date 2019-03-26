#242 Valid Anagram

def isAnagram(self,s,t):

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import re
        for i in range(97,123):
                if len(s)!=len(t):
                        return False
                else:
                        s = re.sub(chr(i), "", s)
                        t = re.sub(chr(i), "", t)
        return True
