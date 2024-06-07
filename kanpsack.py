
# 0-1 Knapsack 

# c capacity of our knapsack
# n no. of items
# wt weight of each corresponding item
# val of each corresponding item

def kanpsack(c,n,wt,val):

    if c==0 or n==0:    #Base condition
        return 0

    elif    wt[n-1] <=c:

        return max(val[n-1]+kanpsack(c-wt[n-1],n-1,wt,val),kanpsack(c,n-1,wt,val))
                #if current element has weight less than capacity we are presented with 2 choices
                #either we select the current element or we don't so we follow the one which has higher val
                
    elif wt[n-1]>c:     #if current element's weight is greater than capacity 
                        #we cant select so just move to next 
        return kanpsack(c,n-1,wt,val)

print(kanpsack(7,4,[1,3,4,5],[1,4,5,7]))