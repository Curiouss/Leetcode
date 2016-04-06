#135 Candy
def candy(self, ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
#List example
# ratings=[2,1,3,1,4,3,0,8]
    L = len(ratings)
    rat =[]
    #Cases for length<3
    if L==0:
       return 0
    elif L==1:
       return 1
    elif L==2:
       if len(set(List))==1:
           return 2
       else:
           return 3

    #Rating dictionary
    def Nov(ratings):
        List = ratings
        Set = list(set(List))
        R = len(Set)
        res ={}
        for i in range(R):
            res[Set[i]]=i+1
        return res

    # Changes

    while ratings != rat:
        rat = ratings[:]
        res = Nov(ratings)
        for i in range(L):
            ratings[i]=res[ratings[i]]
        ratings.append(2147483648)
        for i in range(L):
            ratings[i]=min(min(ratings[i-1],ratings[i+1])+1,ratings[i])
        ratings = ratings[:-1]


    return sum(ratings)