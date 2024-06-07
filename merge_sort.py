
#Reurrence Relation T(n)=2T(n/2)+O(n)
#Time Complexity: O(nlogn) lob base b a=1=c =>T(n)=O(nlogn)
def merge_sort(arr):
    
    #Base case
    if len(arr)==1:
        return arr
    else:
        mid=len(arr)//2
        
        left=merge_sort(arr[:mid])
        right=merge_sort(arr[mid:])
        #merged=merge(left,right)
        #print("Mergeing",left,"and",right,"into",merged)

    #return merged
        return(merge(left,right))       
        
def merge(a,b):     #Merge takes linear time ussing 2 pointers
    c=[]            #for descending order only the merge order will change
    m=0
    n=0

    while m<len(a) and n<len(b):
        if a[m]<=b[n]:
            c.append(a[m])
            m+=1
        else:
            c.append(b[n])
            n+=1
            
    if m<len(a):
        #c.extend(a[m:])
        c[m+n:]=a[m:]
    else:
        #c.extend(b[n:])
        c[m+n:]=b[n:]
    return c
 
if __name__=="__main__":
    xa=[80,33,44,11,19,-5,-9,7,55,0]
    print(merge_sort(a))
    