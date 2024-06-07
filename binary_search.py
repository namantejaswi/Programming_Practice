import math

def binarysearch(arr,target):
    
    low=0
    high=len(arr)-1
    
    while(low<=high):
        
        mid=int((low+high)/2)
        
        if(arr[mid]==target):
            return mid
        
        elif(arr[mid]<target):
            
            low=mid+1            
                
        elif(arr[mid]>target):
            high=mid-1
    
            
l=[2,3,4,5,8,9,11,44,103,124,202,333] 
print(binarysearch(l,11))

print(binarysearch(l,124))

print(binarysearch(l,44))

# print(math.ceil(2.01))
#print(math.ceil(2))

def recurssive_bs(arr,x,low,high)->int:

    mid=math.ceil((low+high)/2)
   
    if(low>high):
        return -1
    
    elif(arr[mid]==x):
        print("Found element at index",mid)
        return mid
    
    elif(x>arr[mid]):
        low=mid+1
        recurssive_bs(arr,x,low,high)
        
    elif(x<arr[mid]):
        high=mid-1
        recurssive_bs(arr,x,low,high)

a=[1,2,3,5,6,7]
        
recurssive_bs(a,6,0,len(a)-1)
recurssive_bs(l,124,0,len(l)-1)
recurssive_bs(l,11,0,len(l)-1)

    