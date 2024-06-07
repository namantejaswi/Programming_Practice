#previous greatest element

nums=[3,5,1,7,3,5,0,6,2]
#[-1,-1,5,-1,7,7,5,7,6]
ans=[-1]*len(nums)

stack=[]

for i in range(1,len(nums)):

    if len(stack)==0:
        ans[i]=-1

    elif stack[-1]>nums[i]:
        ans[i]=stack[-1]

       
    while stack and stack[-1]<=nums[i]:
        stack.pop()

    if len(stack)==0:
        ans[i]=-1

    elif stack[-1]>nums[i]:
        ans[i]=stack[-1]

    stack.append(nums[i])

print(ans)
    