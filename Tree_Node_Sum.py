

class Node:
    def __init__(self,data):
        
        self.data= data
        self.left= None
        self.right= None
   
        
def sum_node_values(root):
   if(root==None):
       return 0
   else: return (root.data + sum_node_values(root.left)+ sum_node_values(root.right)) 
    
    
n7=Node(7) #root
n5=Node(5)
n2=Node(2)
n1=Node(1)
n9=Node(9)

#             7
#           /   \
#          /     \
#         5       9       
#       /   \
#      2     1

n7.left=n5
n7.right = n9
n5.left=n2
n5.right=n1

print("sum of all the nodes is",sum_node_values(n7))


def in_order_traversal(root):
    
    
    if root:
        in_order_traversal(root.left)
        print(root.data)
        in_order_traversal(root.right)        
        
    
in_order_traversal(n7 )
