#135 Candy

#List example

ratings=[2,1,3,3,4,5,6,8]

#Rating dictionary
List = ratings
Set = set(List)
res ={}
[res.setdefault(x,y) for x,y in enumerate(Set)]
