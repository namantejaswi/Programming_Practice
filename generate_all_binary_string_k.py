

#Generate all possible binary strings of length k

def generate(k):
    res=[]
    def  helper(s,k):
        
        if len(s)==k:
            res.append(s)
            return

        helper(s+"0",k)
        helper(s+"1",k)

    helper("",k)
    return res

print(generate(5))
print(generate(3))



