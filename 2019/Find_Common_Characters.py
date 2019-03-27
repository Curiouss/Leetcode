class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        self.li=[]
        for ch in range(97,123):
            self.li.append(chr(ch))
        self.linum=[101]*26
        for st in A:
            self.extract(st)
        out=[]
        for i in range(26):
            if self.linum!=101:
                out+=self.li[i]*self.linum[i]
        return out
        
    def extract(self,string):
        tmp=[0]*26
        for ch in string:
            tmp[self.li.index(ch)]+=1
        self.linum=[min(self.linum[n],tmp[n]) for n in range(26)]
