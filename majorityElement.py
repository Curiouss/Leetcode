##def majorityElement(self, nums):
"""
:type nums: List[int]
:rtype: int
"""
def Comp(List,nums,i):
    CP = True
    j = 0
    while CP==True: 
        if len(List) == j:
            List = List +[nums[i]]+[1]
            return List
            break
        else:
            if List[j] == nums[i]:
                List[j+1] = List[j+1] + 1
                return List
                break
            else:
                j = j + 2
                
def CompN(List,nums,i):
    CP = True
    j = 0
    while CP==True: 
        if len(List) == j:
            List = List +[nums[i]]+[1]
            return 1
            break
        else:
            if List[j] == nums[i]:
                List[j+1] = List[j+1] + 1
                return List[j+1]
                break
            else:
                j = j + 2

nums = [1,2,2,0]
L = len(nums)
Num = L
i = 0
j = 0
N = 0
List = [0]
List[0]= nums[0]
List = List + [0]
while N*2<=Num:
    N = CompN(List,nums,i)
    List = Comp(List,nums,i)
    num = nums[i]
    print(List,N,num)
    i = i+1
print(num)
