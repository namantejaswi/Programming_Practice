
#use a heap to find k closest points to origin

import heapq

def kcloset(points, k):
    heap = []
    for point in points:
        heapq.heappush(heap, (point[0]**2 + point[1]**2, point))
    result = []
    for i in range(k):
        result.append(heapq.heappop(heap)[1])
    return result
    


print(kcloset([[2,1],[1,2],[3,4],[2,1],[1,-1],[2,1]], 2))