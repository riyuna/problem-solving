n=int(input())
L=list(map(int,input().split()))
mx=0
L1=[]
L2=[]
def solve(s,e,l,r):
    global mx
    if s>e:return
    mid=(s+e)//2
    mmx=-10**18
    rem=0
    for i in range(l, r):
        dx=L2[i][0]-L1[mid][0]
        dy=L2[i][1]-L1[mid][1]
        k=0
        if dx>=0 or dy>=0:k=dx*dy
        mmx=max(mmx,k)
        if mmx==k:rem=i
    solve(s,mid-1,l,rem)
    solve(mid+1,e,rem,r)
    mx=max(mmx, mx)
    return mx

