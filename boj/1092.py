n=int(input())
L=list(map(int,input().split()))
m=int(input())
M=list(map(int,input().split()))
L.sort()
M.sort()
if max(L)<max(M):print(-1)
else:
    res=[0]*n
    pt=0
    i=0
    while i<m:
        if L[pt]>=M[i]:
            res[pt]+=1
            i+=1
        else:
            pt+=1
    ct=0
    ans=0
    while True:
        for i in range(n-1,-1,-1):
            for j in range(i, -1, -1):
                if res[j]:
                    res[j]-=1
                    ct+=1
                    break
            if ct==m:break
        ans+=1
        if ct==m:break
    print(ans)