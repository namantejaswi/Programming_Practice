
#Finding median of the array is possible in 0(n) time
#But it is complicated and not very practical
#Thus we take a random,first or middle element as pivot

#Quick sort is an inplace stable sorting algorithm
#In the worst case it takes O(n^2) time but for the average case its O(nlogn)

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]  #Taking first element as pivot as we dont need to update it
        #We can also take the last element len(arr-1) as pivot instead of first element
        #If we take the median elment we have to calculate median for every sub problem
        
        smaller=[i for i in arr[1:] if i < pivot]
        larger=[j for j in arr[1:] if j>=pivot]
        print("Smaller part ",smaller," pivot ",arr[0]," Larger part ",larger)
        print("Present array",arr)
        return quick_sort(smaller)+[pivot]+quick_sort(larger)  
        #We partition the array around the pivot
        
        #print("The sorted array is ",arr)
        
if __name__=="__main__" :
    a=[34,66,17,12,4,67,8,1,99,1,81,0]
    print(quick_sort(a))