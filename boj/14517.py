s=input()
dp=[0]*(len(s)+1)

mod=10**4+7
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i]==s[j]:
            dp[j]+=1
            for k in range(j, len(s)):
                dp[j]+=dp[k+1]
            dp[j]%=mod
ans=sum(dp)%mod
print(ans)