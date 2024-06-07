
lis_1=[1,2,3,4]
lis_2=[5,6,7,8]

l=list(zip(lis_1,lis_2))
print(l)

#Can zip different types like set, tuplles, etc

set_1=(1,2,3)
set_2=(2,3,6)

print(list(zip(set_1,set_2)))