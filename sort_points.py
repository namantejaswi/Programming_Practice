
import math

def calc_angle(x,y):
    r= math.degrees(math.atan2(y,x))
    if r<0: return 360+r
    return r


vectors= [[3,4],[4,3],[-3,4],[-4,-3],[-3,-4],[3,-4],[4,-3],[-4,3]]

res=sorted(vectors, key=lambda x: (x[0]**2+x[1]**2,calc_angle(x[0],x[1])))
import matplotlib.pyplot as plt
plt.scatter(*zip(*res),color=['r','g','b','y','c','m','k','orange'])

print(res)

plt.show()



c=[[1,2],[3,5],[6,2]]

#unpack 2d list

print(*c)