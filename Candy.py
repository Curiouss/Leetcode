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
       if len(set(ratings))==1:
           return 2
       else:
           return 3

    #Rating dictionary
    def Nov(ratings):
        List = ratings
        Set = list(set(ratings))
        Set.sort()
        R = len(Set)
        res ={}
        for i in range(R):
            res[Set[i]]=i+1
        return res

    # Changes
    count =0
    while ratings != rat:
        rat = ratings[:]
        res = Nov(ratings)
        if count == 0:
            for i in range(L):
                ratings[i]=res[ratings[i]]
        ratings.append(2147483648)
        count +=1
        for i in range(L):
            if ratings[i]>max(ratings[i-1],ratings[i+1]):
                ratings[i]=max(ratings[i-1],ratings[i+1])+1
            elif ratings[i]<min(ratings[i-1],ratings[i+1]):
                ratings[i]=1
            elif ratings[i-1]<ratings[i]<=ratings[i+1] or ratings[i+1]<ratings[i]<=ratings[i-1]:
                ratings[i]=min(ratings[i-1],ratings[i+1])+1


        ratings = ratings[:-1]
        print(ratings)
        if ratings[-1]<=ratings[-2]:
            ratings[-1]=1
        if ratings[0]<=ratings[1]:
            ratings[0]=1
        print(ratings)
    
    return sum(ratings)

