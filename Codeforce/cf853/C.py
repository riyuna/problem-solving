import sys
input=sys.stdin.readline

for _ in ' '*int(input()):
    n,m=map(int,input().split())
    L=list(map(int,input().split()))
    ct=dict()
    mem=dict()
    ln=dict()
    for i in L:
        if i not in ct:ct[i]=0
        ct[i]+=1
        mem[i]=0
    for i in range(m):
        p,v=map(int,input().split())
        a=L[p-1]
        L[p-1]=v
        ct[a]-=1
        if ct[a]==0:
            if a not in ln:ln[a]=0
            ln[a]+=(i-mem[a]+1)
        if v not in ct:ct[v]=0
        ct[v]+=1
        if ct[v]==1:
            mem[v]=i+1
    for i in L:
        if i not in ln:ln[i]=0
        ln[i]+=(m-mem[i]+1)
        mem[i]=-1
    res=0
    for i in ln:
        res+=((m+1)*m//2 - (m+1-ln[i])*(m-ln[i])//2)
    print(res)