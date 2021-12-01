import sys
input=sys.stdin.readline
mod=998244353
for _ in ' '*int(input()):
    res=0
    n=int(input())
    L=list(map(int,input().split()))
    dp=[[0,0,0] for i in range(n+1)]
    ct1=0

    for i in L:
        if i==1:ct1+=1
        if i==0:
            dp[i][1]*=2
            dp[i][1]+=1
            dp[i][1]%=mod
        elif i==1:
            dp[i][1]*=2
            dp[i][1]+=dp[0][1]
            dp[i][1]%=mod
        else:
            dp[i][0]*=2
            dp[i][0]+=dp[i-2][1]
            dp[i][0]+=dp[i-2][2]
            dp[i][0]%=mod

            dp[i][1]*=2
            dp[i][1]+=dp[i-1][1]
            dp[i][1]%=mod
        if i+2<=n:
            dp[i][2]*=2
            dp[i][2]+=dp[i+2][0]
            dp[i][2]%=mod
    res+=pow(2, ct1, mod)
    res-=1
    for a,b,c in dp:
        res+=(a+b+c)
        res%=mod
    print(res)