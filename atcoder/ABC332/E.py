import sys
input=sys.stdin.readline
from itertools import combinations
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n,d=linput()
L=linput()
mean=sum(L)/d

total=[0.0]*(1<<n)
for i in range(1<<n):
	for j in range(n):
		if (i>>j)&1:total[i]+=L[j]

bits=[{i} for i in range(1<<n)]
for j in range(n):
	now=1<<j
	for i in range(1<<n):
		if now&i:
			for k in bits[now^i]:bits[i].add(k)
			
for i in range(1<<n):
	bits[i]=(i.bit_count(),i,bits[i])

bits.sort()

dp=[[pow(2,61)-1.0]*(d+1) for i in range(1<<n)]

dp[0][0]=0.0
for ct, i, after in bits:
	if i==0:continue
	for j in range(1, min(ct+1, d+1)):
		ans=(1<<61)-1.0
		for k in after:
			ans=min(ans, (mean-total[k])**2+dp[i^k][j-1])
		dp[i][j]=ans

print(dp[-1][-1]/d)