

lis=[1,2,3]
l=[1,2,3]

print(bool(lis==l))

a=7
print("a is",a," and its address is ",id(a) )
b=10
print("b is",b, "and its address is ",id(b))

a,b=b,a     #Swaping

print("a is",a," and its address is ",id(a))
print("b is",b,"and its address is ",id(b))