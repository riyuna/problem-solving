n=int(input())
L=[]
res=0
for i in range(n):
    h=int(input())
    while(len(L) and L[-1][0]<h):
        tp=L.pop()
        res+=tp[1]
    
    if(len(L)==0):L.append([h, 1])
    elif L[-1][0]==h:
        tp=L.pop()
        res+=tp[1]

        if len(L):res+=1
        tp[1]+=1
        L.append(tp)
    
    else:
        L.append([h, 1])
        res+=1

print(res)