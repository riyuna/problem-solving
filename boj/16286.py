w,n=map(int,input().split())
L=list(map(int,input().split()))

ssum=[0]
for i in L:ssum.append(ssum[-1]+i)

def check(x):
    global w
    n=len(L)
    dp=[0]*(n+1)
    dp[0]=1
    dpsum=[0, 1]

    l,r=0,0
    i=0
    while i<n:
        now=ssum[i+1]
        while now-ssum[l]>w:
            l+=1
        while now-ssum[r]>=w-x:
            r+=1
        # print(i,l,r)
        i+=1
        if dpsum[r]>dpsum[l]:dp[i]=1
        else:dp[i]=0
        dpsum.append(dpsum[-1]+dp[i])
    # print(dp)
    # print(dpsum)
    return dp[-1]==1
    
lo=0
hi=w
while lo<hi:
    mid=(lo+hi)//2
    if check(mid):hi=mid
    else:lo=mid+1

print(hi**2)
