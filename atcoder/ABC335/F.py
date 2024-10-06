import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()
L=linput()

dp=[0]*n
mem=[[0]*(i) for i in range(501)]
dp[0]=1

for i in range(n):
	for j in range(1, 501):
		dp[i]+=mem[j][i%j]
		dp[i]%=mod
	if L[i]<=500:
		mem[L[i]][i%(L[i])]+=dp[i]
		mem[L[i]][i%(L[i])]%=mod
	else:
		for j in range(i+L[i], n, L[i]):
			dp[j]+=dp[i]
			dp[j]%=mod

print(sum(dp)%mod)