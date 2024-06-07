
#                   A----I---J----K
#                 /  \
#                B    C-->H <--| 
#               /|\    \       | 
#              D E F    G------|
#               \   
#                \     
#                 L
#                  |
#                  |
#                  M--->N  
#                  
#   Adjacency list Representation:
# Using dictionary
graph = {'A' : ['B', 'C', 'I'],
         'B': ['A','D', 'E', 'F'],
         'C': ['H','G','A'],
         'D':['L','B'],
         'E':['B'],
         'F':['B'],
         'G':['H','C'],
         'H':['G','C'],
         'I':['J','A'],
         'J':['K'],
         'K':[],
         'L':['M','D'],
         'M':['N'],
         'N':[],
         
         }
         
# Implementing BFS

# The fundamental idea is to start with a arbitrary node and visit all the nodes connected to it.
# Then we move to the next node and visit all the nodes connected to it.

#In order to carry out this procedure we use the qeueue data structure.

# We start with any vertex, enqeue and then start visiting the connected vertices.
# Any connected vertex we encounter, if it is not in the qeue we enqueue it.
# Once all the elments of the neighbours of a vertex are visited, we dequeue it.
# Then we move on to the next vertex present in queue and repeat the process.
         
       
         
def breadth_first_search(graph,start):
    qeue = []
    is_visited=[] 
    res=[] 
       
    qeue.append(start)
    is_visited.append(start)
    
    while(len(qeue)!=0):
        v=qeue.pop(0)
        print("Completely explored ",v)
        
        for neighbour in graph[v]:
            # for an efficient implementation we can index alphabetically the vertices 
            # and use boolean array for constant time lookup instead of linear time 
            if neighbour not in is_visited:     
                is_visited.append(neighbour)
            
                print("The vertex ",graph[v]," is connected to ",neighbour)
                qeue.append(neighbour)
        res.append(v)
        print("The BFS order is ",res)
        

if __name__ == '__main__':
    breadth_first_search(graph,'L')

