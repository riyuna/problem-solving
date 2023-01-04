n,m,k=map(int,input().split())
L=list(map(int,input().split()))
money=[0]*n
dp=[0]*n
mxm=m
for i in range(n):
	money[i]=max(money[i],mxm)
	for j in range(i):
		loan=money[j]*k
		stock=(loan+money[j])//L[j]
		remain=(loan+money[j])%L[j]
		now=stock*L[i]+remain
		if stock:dp[i]=max(dp[i], now)
		money[i]=max(money[i], now-loan)
	if money[i]>mxm:mxm=money[i]
# print(money)
# print(dp)
print(max(max(dp),m))