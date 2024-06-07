

#Subset sum given an array of positive integers and a target
#determine if we can get a subset such that its sum is equal to target

s=11
arr=[2,3,7,8,10]

def subset(s,n,arr):
    
    if s==0:    return True #it is alwasys possible to have zero sum by selecting empty subset
    if n==0:    return False    #if we have no elments only sum zero possible

    if arr[n-1]<=s:

        #we either chooose the elment or we don't choose in any case index moves
        #and if we choose the target subttacted by choosen value
        return subset(s-arr[n-1],n-1,arr) or subset(s,n-1,arr)


    if arr[n-1] > s:    #if element greater than target
        return subset(s,n-1,arr)

print(subset(11,5,arr))
print(subset(14,5,arr))
print(subset(8,5,arr))
print(subset(9,5,arr))


    