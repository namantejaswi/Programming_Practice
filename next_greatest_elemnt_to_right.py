

#next greatest element to the right

arr=[3,9,4,6,1,2,4,11,16,7,1]
res=[-1]*len(arr)

stack=[]



for i in range(len(arr)-1,-1,-1):

    while(stack):

        if stack[-1]>arr[i]:
            res[i]=stack[-1]
            break

        elif arr[i]>stack[-1]:   stack.pop()

    if len(stack)==0:   res[i]=-1   #no greater element found

    stack.append(arr[i])

print(res)