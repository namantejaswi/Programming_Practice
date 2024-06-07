
def smallest_two(arr):

    m1 = float('inf')
    m2 = float('inf')

    for i in arr:

        if i==m1:  continue     #we want unique smallest elements
        if i<m1:   
            if m2!=float('inf') and m1!=float('inf'):
                m2=m1
            m1=i
        

        else: m2=min(m2,i)

    if m2==float('inf'):    print("we only have one unique elment ")

    return (m1,m2)

print(smallest_two([1,5,2,66,3,56,88,11,-1,-2,3,5,-2,-1]))
print(smallest_two([1,1,1,1]))
        
        

         