# def addDigits(self, num):
#     """
#     :type num: int
#     :rtype: int
#     """
num=123
L = len(str(num))
Num = str(num)
sum = 0
for i in range(L-1):
    sum = sum + int(Num[i])
print(sum)