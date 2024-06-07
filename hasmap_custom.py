def solution(queryType, query):
    ans = 0
    hmap = {}
    ck = 0
    cv = 0
    for i in range(len(queryType)):
        cmd = queryType[i]
        quer = query[i]
        if cmd == "insert":
            key,val = quer[0],quer[1]
            hmap[key-ck]=val-cv
        elif cmd == "addToValue":
            k = quer[0]
            cv+=k
        elif cmd == "addToKey":
            k = quer[0]
            ck+=k
        else:
            k = quer[0]
            k-=ck
            val = hmap[k] + cv
            ans = ans + val
    return ans