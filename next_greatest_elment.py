zzzzzzzzzzzzzzzzzzz
#Next greatest element
# 1,4,3,4,7,8,3
# 4,7,4,7,8,-1,-1

nums=[1,4,3,4,7,8,3]
stack=[]
ans=[0]*len(nums)
print(ans)

for i in range(len(nums)-1,-1,-1):

    while stack and stack[-1]<=nums[i]:
        stack.pop()

    if len(stack)==0:
        ans[i]=-1

    elif stack[-1]>nums[i]:
        ans[i]=stack[-1]

    stack.append(nums[i])

print(ans)
