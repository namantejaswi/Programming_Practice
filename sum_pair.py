
arr1=[2,3,4,-2,3,4,5,6]
arr2=[3,4,2,7,4,1,0,-3]
targetsum=8

#Find the number of ways you can sum upto 12

from collections import Counter

dic1=Counter(arr1)
dic2=Counter(arr2)
count=0
res=set()

for i in dic1:

    if targetsum-i in dic2:
        count+=dic1[i]*dic2[targetsum-i]
        res.add((i,targetsum-i))

print(count)
print(res)