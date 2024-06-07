

#Merge 2 sorted array extra space allowed
from typing import List # from 3.9 List is natively thhere


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        """
        nums3=[]
        m1:int
        n1:int
        m1=n1=itr=0
        
        while(m1<m and n1<n):
            if(nums1[m1]<=nums2[n1]):
                nums3.append(nums1[m1])
                m1=m1+1
            elif(nums2[n1]<nums1[m1]):
                nums3.append(nums2[n1])
                n1=n1+1
    
                
        if(m1<m):
            nums3.extend(nums1[m1:m+1])
        elif(n1<n):
            nums3.extend(nums2[n1:n+1])
            
        print(nums3)
        nums1=nums3.copy()
        print(nums1)

if __name__ == '__main__':
    merge([1,2,6,8,9],[3,4,5,6,7])
    
    