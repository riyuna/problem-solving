n=int(input())
L=list(map(int,input().split()))
dp=[[]for i in range(n)]
for i in range(n):
    mx=-1
    pt=-1
    for j in range(i):
        if L[j]<L[i] and len(dp[j])>mx:
            mx=len(dp[j])
            pt=j
    if pt==-1:dp[i].append(L[i])
    else:
        dp[i]=dp[pt][:]
        dp[i].append(L[i])
mx=-1
pt=-1
for i in range(n):
    if len(dp[i])>mx:
        mx=len(dp[i])
        pt=i
print(mx)
for i in dp[pt]:
    print(i,end=' ')