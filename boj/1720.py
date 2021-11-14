dp=[0,1,3]
for i in range(40):
    dp.append(dp[-1]+dp[-2]*2)
n=int(input())
if n==1:print(1)
elif n%2:
    print((dp[n]+dp[n//2])//2)
else:
    print((dp[n]+dp[n//2+1])//2)