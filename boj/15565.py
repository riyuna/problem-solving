n,k=map(int,input().split())
L=list(map(int,input().split()))
ct=0
for i in L:
    if i==1:ct+=1
if ct<k:print(-1)
else:
    cct=0
    for i in range(n):
        if L[i]==1:cct+=1
        if cct==k:break
    res=n
    pt1=0
    pt2=i
    for i in range(ct-k+1):
        while pt1<n and L[pt1]!=1:pt1+=1
        if pt1==n:break
        res=min(res, pt2-pt1+1)
        pt1+=1
        pt2+=1
        if pt2==n:break
        while pt2<n and L[pt2]!=1:pt2+=1
        if pt2==n:break
    print(res)