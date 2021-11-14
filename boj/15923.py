L=[]
for i in ' '*int(input()):
    L.append(list(map(int,input().split())))
res=0
for i in range(len(L)):
    a,b=L[i-1]
    c,d=L[i]
    res+=(abs(a-c)+abs(b-d))
print(res)