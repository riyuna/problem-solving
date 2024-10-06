n=int(input())
s=input()
dp=[[0,0,0,0] for i in range(n)]
mod=10**9+7
ct=0
if s[-1]=='K':dp[-1][3]=1
for i in range(n-2, -1, -1):
    dp[i][1]=dp[i+1][1]
    dp[i][2]=dp[i+1][2]
    dp[i][3]=dp[i+1][3]

    if s[i]=='K':dp[i][3]+=1
    if s[i]=='C':dp[i][2]+=dp[i+1][3]
    if s[i]=='O':dp[i][1]+=dp[i+1][2]
    if s[i]=='R':
        after = pow(2, i, mod)
        ct+=(after*dp[i+1][1])%mod
        ct%=mod

print(ct%mod)