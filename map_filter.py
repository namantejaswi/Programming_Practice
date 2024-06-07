

#The map function applies a given function to each item 
# of a iterable like list, tuble etc and returns an iterator


def cube(x:int)->int:
    return(x*x*x)

def square(x:int)->int:
    return(x*x)

lis=[3,6,6,7,8,9,3,1,8]

m=map(cube,lis) #no ()

print(set(map(square,lis)))

print(list(m))

#lamda functions are commonly used with maps

flip=lambda x:-x
z=(list(map(flip,lis))) 
print(z)

z.extend([1,3,4,5,6])

ispositve=lambda i:i>0

y=list(filter(ispositve,z))
print("After applying filter","\n", y)

#Using lamda fuction within a filter directly

evens=filter(lambda k:(k%2==0),z)

print(list(evens))

