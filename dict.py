

arr=[[1,2,3],[11,22,33]]
arr[0][1]=0
print(arr)


ar=[[10,11],[20,22],[30,33],[4,44],[5,55]]
print(ar)

dic=dict(ar)
print(dic)

for i in dic:
    print("key is",i,"Value is",dic[i])
    
for k,v in dic.items():
    print("key",k,"value",v)
    
players={'van dijk':'liv','de bruyne':'mcl','ronaldo':'rma','ronaldo':'mun'}

for k,v in players.items():
    print(k,v)
    
for k in players: print(k,players[k])

if("van dijk" in players):print("van dijk key is in players")

if("liv" in players):print("van dijk key is in players")

three_d=((0,0,0),(2,3,4),(7,9,17))
print(type(three_d[0]))