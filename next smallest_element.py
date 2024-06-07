                                                                                                                                                                                                                            #next smallest  
nums=[3,5,1,7,3,    5,0,6,2]
#[1,1,0,3,0,    0,-1,2,-1]
ans=[-1]    *len(nums)
stac    k = []


for i in ran    ge(len(nums)-1,-1,-1):
    if l    en(stack)==0:
            ans[i]=-1

    elif     stack[-1]<nums[i]:
            ans[i]=stack[-1]


    whil    e stack and stack[-1]>=nums[i]:
            stack.pop()

    if len(stack)==0    :
        nums[i]=-1  
    elif stack[-    1]<nums[i]:
        ans[    i]=stack[-1]
    stac    k.append(nums[i])

print(ans)