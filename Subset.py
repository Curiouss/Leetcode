class Solution(object):
    def subsets(self, nums):
        Len = len(nums)
        Num = list(set(nums))
        BinNum = 2**Len
        Rlist = list()
        for i in range(BinNum-1):
            Count = bin(BinNum-i-1)
            Nlist = list()
            for j in range(len(Count)-2):
                if Count[-1-j] == '1':
                    Nlist.append(Num[-1-j])
            Rlist.append(Nlist)
        Rlist.append([])
        return(Rlist)


