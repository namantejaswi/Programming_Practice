
lis=[1,1,1,1,2,3,2,2,2,4]

print(set(lis))   
   
   
print(lis.index(3))   #Return first index of value. Raises ValueError if the value is not present.

lis.pop() #Remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.
print(lis)

lis.extend([5,6,7])   #Extend list by appending elements from the iterable.

print(lis)

print(lis.count(1))   #Return number of occurrences of value.

lis.reverse()       #Reverses in place
print(lis)

lis.reverse()
print(lis)

print(list(reversed(lis)))   #Does not modify the list, Returns a reverse iterator over the values of the given sequence. 

print(lis)

lis.sort()


x=set(lis)
print(x)

y={1,1,1,7,9,12}

ins=x.intersection(y)   #Return the intersection of two sets as a new set
print(ins)

